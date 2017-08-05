matrix=[]

while True:
    line=input()
    if not line: break
    values=line.split()
    row=[str(value) for value in values]
    matrix.append(row)
print(matrix)
print(matrix[0])
print(matrix[1])
