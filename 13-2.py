#계산기 클래스
a=int(input("첫번째 숫자를 입력하세요.:"))
b=int(input("두번째 숫자를 입력하세요.:"))

class Calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def plus(self):
        result=self.a+self.b
        return result

    def minus(self):
        result=self.a-self.b
        return result

    def mul(self):
        result=self.a*self.b
        return result
    
    def div(self):
        result=self.a/self.b
        return result

d = Calculator(a,b)
print("덧셈:",d.plus())
print("뺄셈:",d.minus())
print("곱셈:",d.mul())
print("나눗셈:",d.div())


