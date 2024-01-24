import requests
from bs4 import BeautifulSoup


def get_list_of_kin_naver():
    url = 'https://kream.co.kr/search?gender=women&tmp=1706059436630'  # 원하는 URL로 변경하세요
    response = requests.get(url)
    html_source = response.text

    selector = '#__layout > div > div.shop_mobile.content > div:nth-child(6) > div:nth-child(1) > div > div.search_result_list'

    # HTML 소스에서 특정 내용을 추출하는 함수
    # 예를 들어, BeautifulSoup을 사용하여 tbody 내용을 추출할 수 있습니다.
    # 이 부분은 원하는 방식으로 구현하셔야 합니다.
    soup = BeautifulSoup(html_source, 'html.parser')

    selected_elements = soup.select(selector)



    return selected_elements


# 함수 호출
list_of_links = get_list_of_kin_naver()
print(list_of_links)
