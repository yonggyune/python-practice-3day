seasons = ['봄' , '여름' , '가을','겨울']

for season in seasons:
    print(season)


ages = {'Tod' : 35 , 'Jane': 23, 'Paul' : 62}

# key를 가져오는 법
for key in ages.keys():
    print(key)

# value 가져오기
for value in ages.values():
    print(value)

for key in ages.keys():
    print ('{}의 나이는 {}입니다'.format(key,ages[key]))

## dict 에서는 가져오는 값이 대부분 key 값이다.
for key in ages:
    print ('{}의 나이는 {}입니다'.format(key,ages[key]))

for key,value in ages.items():
    print('{}의 나이는 {} 입니다'.format(key,value))

# key와 값이 모두 필요한 경우에는 item이란 함수를 사용하면 되고 
#dic 은 list와 달리 순서가 없다

dict1 = {1:100, 2:200}
dict2 = {1:1000 , 3:300}

dict1.update(dict2)
print(dict1)
### 합집합처럼 사용되는 것이지만 겹치는 경우 update를 시키는 값으로 변환 시켜주시 떄문에  update의 순서가 중요하다
