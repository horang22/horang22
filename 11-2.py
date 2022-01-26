#입력받은 수의 평균

list=[]
sum=0

for i in range(0,7):
    list.append(int(input("정수를 입력해주세요.:")))
    sum+=list[i]

print("평균:",sum/7)
