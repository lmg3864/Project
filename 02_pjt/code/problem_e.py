import requests
from pprint import pprint


def credits(title):
    URL1 = f"https://api.themoviedb.org/3/search/movie?api_key=343a75bf78b2668536902172a1013373&query={title}"
    response = requests.get(URL1).json()
    results = response.get("results")
    # 조건문 이용하여 검색할 수 없는 영화일 경우 None반환
    if results == []:
        return None
    # results 리스트 안에 있는 딕셔너리 중 "id" 
    movie_id = results[0]["id"]
    
    # movie_id 넣어서 링크 연결
    # cast랑 crew가 따로 있으므로 results2, results3 각각 생성
    URL2 = f"https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key=343a75bf78b2668536902172a1013373"
    response2 = requests.get(URL2).json()
    results2 = response2.get("cast")
    results3 = response2.get("crew")

    # 각각의 "cast"와 "crew"에서 빼온 결과 값을 넣어줄 리스트 각각 생성
    cast_list = []
    directing_list = []
    # 반복문 이용하여 cast_id 10 미만일때 cast_list에 "name"값 넣어줌
    # 반복문 이용하여 "department"가 "Directing"인 경우 directing_list에 "name"값 넣어줌
    for i in range(len(results2)):
        if results2[i]["cast_id"] < 10:
            cast_list.append(results2[i]["name"])
    for i in range(len(results3)):
        if results3[i]["department"] == "Directing":
            directing_list.append(results3[i]["name"])

    # 새로운 딕셔너리를 생성해서 cast_list와 directing_list를 합쳐줌
    new_dic = {'cast' : cast_list, 'directing' : directing_list}
    return new_dic
    # 여기에 코드를 작성합니다.  


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화 id를 통해 영화 상세정보를 검색하여 주연배우 목록(cast)과 스태프(crew) 중 연출진 목록을 반환
    영화 id 검색에 실패할 경우 None을 반환
    """
    pprint(credits('기생충'))
    # {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    pprint(credits('검색할 수 없는 영화'))
    # None
