# quiz.py

'''
    아래 형식에 맞춰 문자열을 출력하세요
    내용을 본인의 정보를 출력하고
    각 정보는 변수에 저장한 후에 문자열 포매팅을 활용해보세요
    
    이름 : 000
    나이 : 00살
    키  : 000.0cm
    주소 : 00시 00구 00동
    생년월일 : 0000.00.00
'''

name = '구승현'
age = 25
tall = '182.1cm'
addrsss = '전주시 덕진구 송천동'
test1 = '1998년 09월 05일'
test2 = """이름 : {}
나이 : {}
키 : {}
주소 : {}
생년월일 : {}
"""
print(test2.format(name, age, tall, addrsss, test1))



