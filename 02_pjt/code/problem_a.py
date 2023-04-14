import requests

def popular_count():
    # URL 내용 response에 넣기
    # 내용중 'results' 값 추출하여 reults에 넣기
    # results의 개수로 리턴
    URL = "https://api.themoviedb.org/3/movie/popular?api_key=343a75bf78b2668536902172a1013373"
    response = requests.get(URL).json()
    results = response.get("results")
    return len(results)
    # 여기에 코드를 작성합니다.  


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
