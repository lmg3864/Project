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
