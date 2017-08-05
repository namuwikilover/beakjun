from functools import reduce

list = []

for i in range(9) :     # 난쟁의 키 입력
    list.append(int(input()))
sum = reduce(lambda x , y: x+y, list) #아홉 난쟁이의 키의 합.

for i in range(9) :
    for j in range(9):
        check = sum - list[i] - list[j]
        if check == 100:
            print(check)
            list.pop(i)
            list.pop(j)
            print(list)
            break
