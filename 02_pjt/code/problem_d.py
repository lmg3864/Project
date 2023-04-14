import requests
from pprint import pprint

def recommendation(title):
    # Search Movies
    # 변수 title을 입력 받아야 하므로 f 붙임
    URL1 = f"https://api.themoviedb.org/3/search/movie?api_key=343a75bf78b2668536902172a1013373&query={title}"
    response = requests.get(URL1).json()
    results = response.get("results")
    # 조건문 이용하여 검색할 수 없는 영화일 경우 None반환
    if results == []:
        return None
    # results 리스트 안에 있는 딕셔너리 중 "id" 
    movie_id = results[0]["id"]
    # Get Recommendations
    # results 의 "id" 값 가지고 링크생성
    URL2 = f"https://api.themoviedb.org/3/movie/{movie_id}/recommendations?api_key=343a75bf78b2668536902172a1013373"
    response2 = requests.get(URL2).json()
    results2 = response2.get("results")
    # 새로운 딕셔너리 생성
    # 반복문 이용하여 "results2"의 "title"값만 반환
    title_list = []
    for i in range(len(results2)):
        title_list.append(results2[i]["title"])
    return title_list
    # 여기에 코드를 작성합니다.  


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화의 id를 기반으로 추천 영화 목록 구성
    추천 영화가 없을 경우 []를 반환
    영화 id 검색에 실패할 경우 None을 반환
    (주의) 추천 영화의 경우 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(recommendation('기생충'))
    # ['조커', '1917', '조조 래빗', ..생략.., '살인의 추억', '펄프 픽션']
    pprint(recommendation('그래비티'))
    # []
    pprint(recommendation('검색할 수 없는 영화'))
    # None
