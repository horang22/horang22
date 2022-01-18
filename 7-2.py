#1. 1부터 100까지의 수 중에서 짝수이면서 7의 배수가 아닌수:[]개

num=0

for i in range(1,101):
    if (i%2)==0 and (i%7)!=0:
        num+=1
print("1부터 100까지의 수 중에서 짝수이면서 7의 배수가 아닌 수:",num,"개")




#2.0이 입력될 때까지 숫자를 계속 입력 받아 입력 받은 숫자들의 합을 출력하는 프로그램 만들기

number=0
sum=0

while True:
    number=int(input("숫자를 입력하세요:"))
    sum+=number

    if number==0:
        print(sum)
        break
    
