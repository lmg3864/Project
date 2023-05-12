<template>
  <div>
    <div class="card h-100">
        <img v-if="imgSrc" :src="imgSrc" class="card-img-top"   alt="">
        <div class="card-body">
            <h2 class="card-title fw-bold">{{movie.title}}</h2>
            <p class="card-text" style="overflow: hidden; white-space:nowrap; text-overflow:ellipsis;">{{movie.overview}}</p>
        </div>
    </div>
  </div>
</template>

<script>
export default {
    name: 'MovieCard',
    props: {
        movie : Object
    },
    data(){
        return {
            imgSrc: "https://image.tmdb.org/t/p/w500" + this.movie.poster_path
        }
    },
}
</script>

<style>

</style>