#정수 n까지의 합을 구하는 함수 만들기



def numSum(n1):
    sum=0
    for i in range (0,n1+1):
        sum+=i
    return(sum)

number=int(input("정수를 입력하세요:"))
result=numSum(number)
print(result)