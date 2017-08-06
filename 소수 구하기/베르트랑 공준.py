# https://stackoverflow.com/questions/6687296/python-sieve-of-eratosthenes-compact-python
def pgen(n): # Sieve of Eratosthenes generator by Dan Salmonsen
    yield 2
    np = set()
    for q in range(3, n+1, 2):
        if q not in np:
            yield q
            np.update(range(q*q, n+1, q+q)) 

l=[]
while True:
    n=int(input())
    if n==0: break
    l.append(n)

for i in range(len(l)):
    print(len([value for value in list(pgen(2*l[i])) if value>l[i]]))
