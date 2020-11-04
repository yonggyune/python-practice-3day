def get_web(url) :
    """URL을 넣으면 페이지 내용을 돌려주는 함수
    """
    import urllib.request
    response = urllib.request.urlopen(url) #받은 url을 열고 
    data = response.read() #읽고
    decoded = data.decode('utf-8') #사람이 볼수 있게 디코딩 하고
    return decoded #돌려주는 함수

url = input('웹 페이지 주소?')
content = get_web(url)
print(content)


"""
미리 만들어진 코드를 가져와 쓰는 방법
import 모듈
모듈안에 함수를 쓰기위해서는
모듈.함수 식으로 사용한다
"""
