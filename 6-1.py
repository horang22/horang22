#[비교연산자와 조건문]

a=10
b=7

print(a>=b)
print(a==b)
print(a!=b)

#[논리연산자]

x=10
y=False

print(x>=10 and y==False)  #a와 b 모두 참이면 참
print(x<10 or y==False) #a와 b 둘 중 하나만 참이면 참
print(not y) #a가 거짓이면 참, a가 참이면 거짓

#[조건문] : 이후 tab 필수

m=3000

if m>=5000:
    print("결제 가능")
else:
    print("결제 불가능")

line="Hello World"

if "Hello" in line:             #if a in b
    print("Hello o")

else:
    print("Hello x")

