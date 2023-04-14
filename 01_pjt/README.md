problem_a

처음에는 터미널 사용과 다른 파일에서 가져오는 것이 어려웠지만 다른 파일에 있는 값들을 손쉽게 불러와서 딕셔너리에 넣는것을 알게 되었다.

```python
import json
from pprint import pprint


def movie_info(movie):
    dict_a ={'id' : movie.get('id'), 'title' : movie.get('title'), 'poster_path' : movie.get('poster_path'), 'vote_average' : movie.get('vote_average'), 'overview' : movie.get('overview'), 'genre_ids' : movie.get('genre_ids')}
    return dict_a


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='utf-8')
    movie_dict = json.load(movie_json)
    
    pprint(movie_info(movie_dict))

```

-------------------------

problem_b

한 파일을 불러와서 그 파일 값을 다른 파일을 이용하여 값을 주는것이 어려웠지만 차근차근 딕셔너리를 생성하고 반복문을 활용하여 원하는 곳에 알맞은 값을 넣어주는 법을 알게 되었다.

``` python

import json
from pprint import pprint


def movie_info(movie, genres):
    movie_dict = {'genre_names' : movie.get('genre_names'), 'id' : movie.get('id'), 'overview' : movie.get('overview'), 'poster_path' : movie.get('poster_path'), 'title' : movie.get('title'), 'vote_average' : movie.get('vote_average')}
    genre_ids = movie["genre_ids"]
    movie_dict["genre_names"] = []

    #영화의 장르 아이디를 가지고
    #장르의 이름을 가져올 수 있는지
 
    for id in genre_ids:
        # 장르 id 확인

        #장르 id와 일치하는 장르 정보가 있으면 "name" 값 추출
        for genre in genres:
            if id == genre["id"]:
                #id를 찾았으나 그 id의 장르 이름을 추가
                movie_dict["genre_names"].append(genre["name"])
    
    return movie_dict

        

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='utf-8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))


```

----------------------

problem_c

b에서 만들어 놓은 함수르 가져와서 사용하면 보다 쉽고 간단하게 코딩을 할 수 있음을 알게 되었고 반복문 이용하여 마무리 할 수 있었습니다.

```python

import json
import problem_b
from pprint import pprint


def movie_info(movies, genres):
    movie_list = []
    for movie in movies:
        movie_list.append(problem_b.movie_info(movies, genres))
    return movie_list

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))


```

-----------

problem_d

파일 경로를 입력하여 파일을 불러오고 모르는 함수 사용하는게 힘들었습니다. 함수 안에 내용을 담고 반복문을 사용하여 워하는 기능을 추가할 수 있었습니다.

```python

import json


def max_revenue(movies):
    revenue_list = {}
    for movie in movies:
        id = movie.get('id')
        title = movie.get('title')
        movieJson = open('data/movies/'+str(id)+'.json', encoding='utf-8')
        movieJson = json.load(movieJson)
        revenue = movieJson.get('revenue')
        revenue_list[revenue] = title
    maxrevenue = max(revenue_list.keys())
    maxrevenueMovie = revenue_list.get(maxrevenue)
    return maxrevenueMovie
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)
    
    print(max_revenue(movies_list))


```

--------------------

problem_e



```python

import json


def dec_movies(movies):
    decMovies = [] 
    for movie in movies:
        id = movie.get('id')
        title = movie.get('title')
        movieJson = open('data/movies/'+str(id)+'.json', encoding='utf-8')
        movieJson = json.load(movieJson)
        date = movieJson.get('release_date')
        start = date.find('-')
        end = date.find('-', start+1)
        month = date[start+1:end]
        if month == '12':
            decMovies.append(title)
    return decMovies

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)
    
    print(dec_movies(movies_list))


```