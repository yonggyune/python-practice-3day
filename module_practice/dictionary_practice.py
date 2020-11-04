wintable = {
    '가위' : '보',
    '바위' : '가위',
    '보' : '바위'
    }

print(wintable['가위'])




## dict 의 경우 앞이 key 뒤가 value 로 서로 이어짐

def rsp(mine,yours):
    if mine == yours:
        return 'draw'
    elif wintable[mine] == yours:
        return 'win'
    else:
        return'lose'


a= input('what is your choice? ')
b= input('what is other choice? ')
result = rsp(a,b)

messages ={
    'win' : '이겼다',
    'draw' : '비겼다',
    'lose': '졌다'}

print(messages[result])

#### dic 에서 key 값에는 보통 문자열 숫자 튜플 을 사용할 수 있는데 값으로는 모두 가능 list도 사용가능하다
"""
dict 에서 값을 수정하기 위해서는 dict[key 값] = 수정값 을통해 값을 변화 시키면 된다
값을 추가 하기 위해서는 list 와 달리 append 를 사용하지 않고 수정시킬때와 같이 새로운 key 값에 값을 넣어서 대입하면 된다
값을 삭제 하기 위해서는 del (dict[]) 을 사용하던지 dict.pop() 을 쓰면 가능 이떄 pop은 뽑아내서 저장 하는 기능
list 에는 remove 함수가 있으나 dict 에는 remove 함수가 없다
"""