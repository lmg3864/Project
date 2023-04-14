# problem_a 

def popular_count():
    # URL 내용 response에 넣기
    # 내용중 "results" 값 추출하여 reults에 넣기
    # results의 개수로 리턴
    URL = "https://api.themoviedb.org/3/movie/popular?api_key=343a75bf78b2668536902172a1013373"
    response = requests.get(URL).json()
    results = response.get("results")
    return len(results) 

# 외부 사이트에서 링크를 따와서 자료를 받아오는 방법을 알게되었고 그 받아온 자료를 가지고 원하는 값만을 추출해서 사용하는것이 어려웠지만 지금까지 배웠던 내용을 가지고 results 개수를 반환할 수 있었습니다.

---------------------

# problem_b

def vote_average_movies():
    URL = "https://api.themoviedb.org/3/movie/popular?api_key=343a75bf78b2668536902172a1013373"
    response = requests.get(URL).json()
    results = response.get("results")
    # 새 딕셔너리 생성
    average = []
    # 반복문 이용하여 "results"안에있는 내용 반복
    # 조건문 이용하여 "results" 요소 중 "vote_average"가 8이 넘는 i만 새 딕셔너리에 추가
    for i in range(len(results)):
        if results[i]["vote_average"] > 8 :
            average.append(results[i])
    return average

# 받아온 자료를 반복문과 조건문을 이용하여 원하는 값만 추출하는 것을 배웠습니다. 딕셔너리 안에 리스트가 있고 그 리스트 안에 또 딕셔너리가 있는 형태여서 for문과 if문을 짤때 힘들었지만 각각의 문법에 맞추어 내장함수를 활용하여 원하는 값을 추출할 수 있었습니다.

-------------------

# problem_c

def ranking():
    URL = "https://api.themoviedb.org/3/movie/popular?api_key=343a75bf78b2668536902172a1013373"
    response = requests.get(URL).json()
    results = response.get("results")
    # 불러온 results를 key값이 "vote_average"를 기준으로 내림차순
    results.sort(key = lambda x : x["vote_average"], reverse= True)
    # 상위 5개영화만 반환
    return results[:5]

# 받아온 자료를 sort라는 배열해주는 함수를 사용하여 상위 5개 영화를 출력하는 것을 배웠습니다. 단순히 리스트가 아닌 리스트 안에 있는 딕셔너리의 한 요소를 기준으로 해야해서 어려웠지만 리스트 안의 딕셔너리 key값을 선언해주고 그것을 기준으로 내림차순 해주고 상위 5번째까지만 반환하여 해결하였습니다.

-----------

# problem_d

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

# 입력을 받아 링크에 넣어서 안에 있는 자료중 필요한 것만 뽑아서 변수에 넣어주고 그 값을 또 링크에 넣어서 원하는 값을 추출하는 것을 배웠습니다. 그리고 조건문 이용하여 검색할 수 없는 영화일 경우 None을 반환하고 다른값을 입력하면 빈 값이 나오게 하는 것을 배웠습니다. 링크를 불러오고 거기서 값을 추출하고 또 그 값을 가지고 링크에 넣고 원하는 값을 얻는것이 어려웠지만 f formatting을 이용하여 변수를 넣어서 받아오고 반복문을 이용하여 축적시켜 원하는 결과값을 얻을 수 있었습니다.

-----------

# problem_e

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

# 입력을 받아 링크에 넣어서 연결시켜 값을 추출하고 그 추출된 값을 또 입력으로 넣고 새 링크에서 원하는 결과값을 얻어와 반복문과 조건문으로 필터를 거쳐서 올바른 출력을 내는 것을 배웠습니다. 새 링크에서 원하는 값이 두 종류여서 리스트를 따로 지정하고 받아주고 반복문과 조건문으로 필터링 하는것이 힘들었지만 배웠던 내용을 가지고 딕셔너리 - 리스트 - 딕셔너리 구조에서 원하는 값을 추출해서 함수를 사용하여 올바른 결과를 낼 수 있었습니다.