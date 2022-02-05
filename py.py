


from tokenize import Number


if 4 in [1, 2, 3, 4]:
    print('4가 있습니다')

a = 1
b = 2
print(a+b)
print(a-b)
print(a*b)
print(a/b) 
print(a%b)

p = 'abc'

print(type(p))
print(p)
print(p[0])

# a[ : : ]
#   이상 : 미만 : 간격
c = 'hobby'

print(c.count('b'))
print(c.find('b'))
print(c.find('x'))

t1 = (1,2,'a','b')
t3 = (3,4)
print(t1+t3)

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])
print(s1 & s2)

money = True
if money:
    print('택시를 타고 가라')
else:
    print('걸어 가라')
print()


score = 70
if score >= 60:
    message = 'seccess'
else:
    message = 'failure'
print(message)
print()

treeHit = 0
while treeHit < 10:
    treeHit = treeHit +1
    print('나무를 %d번 찍었습니다.' % treeHit)
    if treeHit == 10:
        print('나무가 넘어갑니다')
print()

coffee = 10
money2 = 300 
while money2:
    print('돈을 받았으니 커피를 줍니다.')
    coffee = coffee -1
    print('남은 커피의 양은 %d개입니다.' % coffee)
    if not coffee:
        print('커피가 다 떨어졌습니다 판매를 중지합니다.')
        break

test_list = ['one', 'two', 'three']
for i in test_list:
    print(i)
print()

marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks:
    number = number + 1
    if mark >= 60:
        print('%d번 학생은 합격입니다.' % number)
    else:
        print('%d번 학생은 불합격입니다.' % number )
print()

class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
        
class MoreFourCal(FourCal):
    pass

v = FourCal(4,6)
v.setdata(4,6)
print(v.first)
print(v.second)
print(v.add())