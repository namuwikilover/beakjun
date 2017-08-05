number = 123458

def cipher(number):
    li=[]
    while number>0:
        li.append(number%10)
        number=int(number/10) #10으로 나눴더니 float형이 반환된다.
    return li

#print(type(cipher(number)))

print(cipher(number))
