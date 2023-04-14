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
