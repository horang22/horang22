#붕어빵의 틀, 클래스
#[클래스]

#클래스=붕어빵 틀/ 객체=붕어빵

#각각의 개체는 고유의 기능과 성격을 가짐, 서로 다른 객체들에 영향 안미침

from distutils.command.build_scripts import first_line_re


class Waffle:
    pass   #아무 코드가 정해지지 않았을 때 코드 대신 넣어줌

#객체명=클래스이름()

choco=Waffle() #choco 객체 생성
banana=Waffle() #banana 객체 생성

#인스턴스는 어떤 클래스의 객체인지, 관계에 초점을 맞춘 용어
#choco는 waffle의 인스턴스
"""
class Calculator:
    def setdata(self,first,second):
        self.first=first             #self는 setdata함수를 불러온 객체 a를 전달한다.
        self.second=second
    def add(self):
        result=self.first+self.second
        return result

a=Calculator()
a.setdata(6,3)  #a는 self로 전달/6-first/3-second
print(a.add())

'''add 메소드 실행 순서

1️⃣ a.add() 코드를 통해 add 메소드를 불렀습니다.

2️⃣ self에 a 객체를 넣어줍니다. ( result = a.first + a.second )

3️⃣ result라는 변수에 덧셈 결과를 저장해줍니다. ( result = 9 )

4️⃣ 결과가 담긴 result를 리턴해줍니다. ( return result ▶ return 9  )

6️⃣ 결과 값을 출력합니다. ( print(a.add()) ▶ print(9) )
'''
#객체 변수 출력

print(a.first)

b=Calculator()
b.setdata(20,10)
print(b.first)

"""
'''
· 각 연산의 메소드 만들기 (ex. add(self): )

· 각 연산의 연산자를 이용해 결과에 저장 (ex. result = self.first + self.second)

· 클래스 밖에서 해당 메소드 호출 및 출력으로 확인
'''

#[생성자]

class Calculator:
    def __init__(self,first,second):
        self.first=first
        self.second=second

    def add(self):
        result=self.first+self.second
        return result

a = Calculator(6,3)
print(a.add())

'''
✔ 클래스

붕어빵 틀에 비유
✔ 객체 

틀에서 나온 여러가지 다양한 붕어빵에 비유
✔ 인스턴스

어떤 클래스의 객체일 때 쓰는, 객체의 다른 말
✔ 메소드

클래스 안에 있는 함수
✔ 생성자 사용

setdata보다 안전한 방법
'''