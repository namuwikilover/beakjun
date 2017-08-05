height=int(input())
for row in range(height-1, 0, -1):
    print(((row+1)*'*').rjust(height))
print('*'.rjust(height))
