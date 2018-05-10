import requests
from bs4 import BeautifulSoup
import lxml

def crawl_practice():
    req = requests.get('https://www.naver.com/')

    html = req.text

    soup = BeautifulSoup(html,'lxml')

    real = soup.select(
        'div > a'
    )
    """
    div 태그안에 있는 a 태그를 선택해줍니다.
    """
    print(real)

def crawl():
    req = requests.get('https://www.naver.com/')
    # requests.get 을 통해 연결이 가능합니다.
    html = req.text
    # 위의 req 변수 자체는 해당 웹사이트와의 연결상태를 보여줍니다.
    # req.text 형태로 해주면 html코드로 나타내어 줍니다.

    soup = BeautifulSoup(html,'lxml')
    # lxml은 문서코드를 읽어주는 도구(parser) 중 하나입니다.
    # 이 것을 parsing 이라 합니다.

    #real = soup.find("div", class_='ah_list PM_CL_realtimeKeyword_list_base')
    # div태그 중 class이름이 'ah_list PM_CL_realtimeKeyword_list_base' 인 것만을 골라줍니다.

    #real = soup.find("li", class_='ah_item')
    # li 태그 중 class이름이 'ah_item' 인 것만을 골라줍니다.

    real = soup.find_all('span', class_='ah_k')
    # class는 파이썬의 예약어이기 때문에 class_ 라고 써줘야 beautifulSoup라는 라이브러리에서 인식이 가능하다.
    # 단순히 class 라고 써버리면 파이썬의 클래스로 알아들어 오류가 발생한다

    print(real)
    all_list = []
    for i in real:
        #print(i.text)
        # 변수.text 는 태그에서 사람들이 볼 수 있는 텍스트만을 출력해줍니다.
        all_list.append(i.text)
        # i의 텍스트가 all_list라는 리스트 변수에 하나씩 저장된다.
        # -> 여기까지 하면 [<span class="ah_k">현도훈</span>, <span class="ah_k">황현희</span>, 와 같이 뜰텐데
        # i.text 와 같이 text를 쓰면 사람이 바로 볼 수 있는 글자만 나타내준다.

    for number, info in enumerate(all_list):
        if number >= 20:
            break
        print(info)

if __name__ == "__main__":
    crawl()

"""
if __name__== "__main__":
이 파일 자체를 자체적으로 실행할때만 조건문이 작동합니다.
다른 파일에서 이 파일을 불러오면 위의 조건문이 작동하지 않습니다.
"""

