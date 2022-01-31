# ex01.py
'''
    여기는 원래 문자열을 표현하는 공간인데
    여러줄로 주석형탤르 만들려면 사용하기도 한다
'''
'''
    컴퓨터를 구성하는 주요 핵심 장치
    - CPU (central processing unit, 중앙 처리 장치)
    - 입력장치 ( 주 기억장치, RAM)
    - HDD, SSD (보조기억장치)
    출력장치
    입력장치
'''



# 자료형(data type)

n1 = 10                #정수 
n2 = 3.14              #실수
name = 'ITBANK'        #문자열
todayIsSunday = False  #논리값

# 계산기가 베이스므로, 숫자에는 별다른 표실를 하지 않는다

# 문자열은 따옴표로 묶어준다
# '', "", ''' ''', """ """,

# 논리값은 True 혹은 False 만 넣을 수 있다
print(type(10))
print(type(3.14))
print(type('ITBANK'))
print(type(False))

# 컴퓨터는 데이터를 입력받아서 처리하고, 출력하는 과정을 거친다
# 이때 데이터의 종류가 다양할 수 있고
# 컴퓨터는 숫자를 기본으로 생각하니까, 데이터의 유형을 구분해야한다

### 변수 ###
# 컴퓨터가 계산할 수 있도록 미리 데이터를 메모리 일정공간에 준비할 수 있다
# 이때 데이커가 저장되는 메모리의 일정 공간을 코드에서 변수라고 한다
# 데이터를 저장할 수 있는 [공간] 
# 변수는 동사에 하나의 데이터만 저장할 수 있다 
# 추가로 데이터를 저장하면 기존의 데이터가 사라진다 (덮어씌워진다)

n1 = 10          # n1 변수에 10을 저장한다
print(n1)        # n1 변수에 담긴 값을 출력한다

print(n1, n2, name, todayIsSunday)
# 어떤 값을 저장해두었다가, 나중에 불러와서 사용하기 위해서 변수를 사용

