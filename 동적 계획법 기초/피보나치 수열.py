def fibonacci(number):
    if number==1:
        return 0
    elif number==2:
        return 1
    return fibonacci(number-2)+fibonacci(number-1)

number = int(input())
