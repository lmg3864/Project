# 09_pjt

구현 과정 중 학습한 내용

    TMDB API를 사용하여 최고 평점 영화 데이터를 받아오기

    axios 요청으로 받아온 movies를 v-for를 이용하여 영화 하나하나 가져오기 이때 :key="movie.id" 처럼 키 설정 반드시 필요(id는 전부 다른값이므로 key로 movie.id 사용)

    시작하기 전에 컴포넌트 구조랑 router 구조 파악하고 미리 구성 해주고 시작하기

어려웠던 부분

    axios 요청으로 TMDB API키를 선언 해주고 `https://api.themoviedb.org/3/movie/top_rated?api_key=${API_KEY}&language=ko-kr`에서 get으로 데이터 받아오기

    props로 받아올때 받아온 v-for로 나온 movie의 데이터 타입이 객체 이므로 props: {movie : Object}
    그 후 받아온 것 영화 template에서 {{}}사용하여 영화 제목은 movie.title 영화 내용은 movie.overview 으로 사용해주기

    data는 함수이므로 return으로 데이터 주기

새로 배운 것들 및 느낀점

    then에서 받아온 res를 화살표 함수 사용하여 null값인 movies를 선언해주고 그곳에 받아온 영화 데이터 넣어주기 (this.movies = res.data.results)

    그 후 초기 화면으로 넣어주어야 하므로 created에 this.getTopMovies()으로 데이터 출력