#리스트

ex_list=[1,2,3,4,5]

print(ex_list[0])

for i in range(0,len(ex_list)):
    print(ex_list[i])
for i in ex_list:
    print(i)

    #list[a:b] a값부터 b값까지 슬라이싱

#마지막에 값 삽입:append
#특정 인덱스에 값 삽입:insert

ex_list.append(8)
print(ex_list)

ex_list.insert(1,8)
print(ex_list)

#제거:del,remove

del ex_list[2] #2번 값 제거
ex_list.remove(1)
print(ex_list)
