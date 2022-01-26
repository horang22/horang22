#딕셔너리

dic={1:"python",2:"c",3:"java"}

#key:value

print(dic[2])

#데이터 key:value 한번에 추가

dic["d"]="c++"
print(dic)

#dic.update({}) 한번에 넣기

#삭제하기

# del dict["d"]

#key와 value 따로 모아보기

dict.keys()
dict.values()

#깔끔하게 리스트로 변환
list(dict.keys())