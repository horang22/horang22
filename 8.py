#BMI 결과보기

height=float(input("키를 입력하세요.:"))/100
weight=float(input("몸무게를 입력하세요.:"))

bmi=weight/(height**2)

if bmi>=25:
    print("비만입니다.")
elif bmi>=23 and bmi<25:
    print("과체중입니다.")
elif bmi>=18.5 and bmi<23:
    print("정상체중입니다.")
else:
    print("저체중입니다.")