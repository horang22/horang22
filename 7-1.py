#[반복문]

#for문은 리스트, 튜플이랑 자주 쓰임, 이번엔 range
for i in range(10):  #for 변수 in range(시작숫자, 끝):
    print(i)         #수행문

#[이중 반복문]
for i in range(2,10):    #2부터 9까지 반복
    for j in range(1,10): #i에 대해 1부터 9까지 반복
        print(i*j,end="") #줄바꿈 없앰
    print('') #한 줄 출력이 끝나면, 빈값을 출력해 줄바꿈


#[while]
 #while 조건문:
 #    실행문

count=0

while count<10:
    print(count)
    count+=1

#[무한반복문]

#while True:
 #   print("Hello World")

number=0

while True:
    print("문을 여시겠습니까? 1:yes/ 2:no")
    number=int(input())

    if number==1:
        print("문이 열렸습니다.")
    elif number==2:
        break    #프로그램 종료