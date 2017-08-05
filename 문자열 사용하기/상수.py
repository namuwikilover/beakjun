number1, number2 = input().split()
if int(str(number1)[::-1]) > int(str(number2)[::-1]):
    print(int(str(number1)[::-1]))
else:
    print(int(str(number2)[::-1]));
