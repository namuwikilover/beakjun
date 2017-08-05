def findD(a, b) :
    d = 0
    tmp = a % b
    if(tmp == 0) :
        return b
    else:
        d = findD(b, tmp)
    return d;

a = lambda x,y:x*y/findD(x,y)
print(a(6,10))
#print(60/findD(6,10))

# 최소공배수는 a * b / d <- GCD
'''
두 정수 a, b의 최대공약수를 g, 최소공배수를 l 이라고 하면 다음이 성립한다.

(1) a = ga′, b = gb′ (단, a′, b′는 서로소)
(2) l = ga′b′
(3) lg = ab
(4) a = ga′, b = gb′ 일 때 a ± b′ = g(a′ ± b′)
(5) 두 정수 a, b의 모든 공약수는 g의 약수이다.
(6) 두 정수 a, b의 모든 공배수는 l의 배수이다.


위 성질을 이용해서 최소공배수도 쉽게 구할 수 있다.
'''
