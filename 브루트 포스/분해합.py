num = 12345

def sum(num) :
    num = int(num)
    if num == 0:
        return 0
    else:
        return num % 10 + sum(num / 10)

r = sum(num)

print(r)
