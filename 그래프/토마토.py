from queue import *

def main():
    matrix=[]
    while True:
        line=input()
        if not line: break
        values=line.split()
        row=[int(value) for value in values]
        matrix.append(row)
    q=Queue()
    result=q.get()



if __name__=='__main__':
    main()
