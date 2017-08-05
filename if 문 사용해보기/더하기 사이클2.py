n = int(input())

def check(n) :
    n=str(n)
    prev_n=int(n[0])+int(n[1])
    new_n=[]
    new_n.append(n[1])
    new_n.append(str(prev_n[0]))
    s=''.join(new_n)
    return int(s)

def main():
    check_number = n
    save=n
    while True:
        save=check(save)
        if check_number == check(save) :
            break
            save=save

if __name__ == '__main__':
    main()




