n=int(input()); c=0; a=0; b=0; count=0; add=0
add=n

while add!=n or c==0:
    a=int(add/10); b=add%10; c=(a+b)%10
    a=b; b=c;
    add=a*10+b
    count+=1
    
print(count)






