<template>
  <div>
    <h1>{{weather}}한 날씨에는 "{{randomMovie?.title}}" 어때?</h1>
    <div class="d-grid gap-2 mx-auto" style="max-width: 18rem; margin: 0 auto;">
        <button class="btn btn-success" @click="randomPick">Pick</button>
    </div>
    <br>
    <div class="card border-info mb-3" style="max-width: 18rem; margin: 0 auto;">
        <div class="card-header">            
            <img v-if="imgSrc" :src="imgSrc" class="card-img-top" alt="">
        </div>
        <div class="card-body">
            <h5 class="card-title">{{randomMovie?.title}}</h5>
            <p class="card-text"></p>
        </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import _ from 'lodash'

export default {
    name: 'RandomView',
    data() {
        return {
            movies: null,
            randomMovie: null,
            imgSrc: null,
            weather: null,
            
            // 날씨에 따른 장르 id 추천 목록 obj
            recommend : {
                "clouds" : [80, 99, 10752, 878],
                "rain" : [27, 53, 9648, 80, 28],
                "snow" : [18, 16, 10751, 10749],
                "clear" : [37, 10770, 36, 10402, 35],
            }
        }
    },
    methods: {    
        // 날씨 정보 가져오기    
        getWeather() {
            axios({
                method: 'get',
                url: `https://api.openweathermap.org/data/2.5/weather?q=Seoul,kor&appid=${process.env.VUE_APP_WEATHER_API_KEY}`
            })
            .then((res) => {
                this.weather = res.data.weather[0].main
            })
            .catch((err) => {
                console.log(err)
            })
        },

        // 영화 정보 가져오기
        getMovies() {
            axios({
                method: 'get',
                url: `https://api.themoviedb.org/3/movie/top_rated?api_key=${process.env.VUE_APP_MOVIE_API_KEY}&language=ko-kr`
            })
            .then((res) => {
                this.movies = res.data.results

                // 처음 로딩 될때는 아무 영화 추천
                this.randomMovie = _.sample(this.movies)
                this.imgSrc = "https://image.tmdb.org/t/p/w500" + this.randomMovie.poster_path
            })
            .catch((err) => {
                console.log(err)
            })
        },

        // 날씨에 따른 영화 목록 뽑아오기
        recommendPick() {
            if(this.weather) {
                if (this.weather.toLowerCase().trim() in this.recommend){
                    const recommend_genre = this.recommend[this.weather.toLowerCase().trim()]
                    const rec_list = this.movies.map((movie) => {
                        
                        let check = false
        
                        movie.genre_ids.forEach((e) => {
                            if (recommend_genre.includes(e)){
                                check = true
                            }
                        })
        
                        if (check) {
                            return movie
                        } else {
                            return null
                        }
                    }).filter((movie) => movie !== null)
                    this.randomMovie = _.sample(rec_list)
                }else {
                    this.randomMovie = _.sample(this.movies)
                }
            }
        }, 

        // 버튼 누를떄마다 날씨에 따른 랜덤 영화 뽑아오기
        randomPick() {
            this.recommendPick()
            this.imgSrc = "https://image.tmdb.org/t/p/w500" + this.randomMovie.poster_path
        }
    },
    created() {
        this.getWeather()
        this.getMovies()
    }
}
</script>

<style>

</style>