#숫자로 생일을 입력받아 연도와 월,일 출력

bd=input("생일을 입력해주세요.")

print(bd[:4] + "년")
print(bd[4:6] + "월")
print(bd[6:] + "일")

bd=int(input("생일을 입력해주세요."))

print(str(bd//10000) + "년")
print(str(bd%10000//100) + "월")
print(str(bd%100) + "일")