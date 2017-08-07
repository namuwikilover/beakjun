N=int(input()); l=list(map(int, input().split())); m=list(map(int, input().split())); 
l.sort(); m_reverse=sorted(m, reverse=True)
print(sum([a*b for a,b in zip(l,m_reverse)]))
