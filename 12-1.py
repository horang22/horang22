#[튜플] ()둘러쌈, 리스트와 다르게 값을 바꿀 수 없음

ex_tuple1=(1,2,3)
ex_tuple2=(4,5,6)

plus=ex_tuple1 + ex_tuple2

print(plus)

#함수 리턴값을 한꺼번에 여러 개 받을 수 있음

def minmax(a):
    return min(a),max(a)

result=minmax(plus)
print(result)

#집합생성
set1={1,2,5,5,3,7}
set2=set("Hello")
set3={1,4,5}

print(set1)
print(set2)
#집합은 생성될때, 중복된 값 허락x, 순서

#교집합
print(set1&set3)
print(set1.intersection(set3))

#합집합
print(set1|set3)
print(set1.union(set3))

#차집합
print(set1-set3)
print(set1.difference(set3))

#집합과 관련된 함수

#1.값추가
set1.add(8)
set1.update([1,9,8]) #여러개 추가

#2.값제거
set1.remove(1)
