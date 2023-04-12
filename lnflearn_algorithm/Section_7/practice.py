N = int(input())
a, b = 3, 5
r1 = 0
r2 = 0
while True:
    t1 = (N//b)
    t2 = (N-b*(N//b)//a)
    r1 = t1+t2
    if b*t1+a*t2 != N:
        print(-1)   
    t1 = (N//a)
    t2 = 0
    r2 = t1
    if b*t1+a*t2!= N:
        print(-1)       
    res = min(r1, r2)
    print(res)
    break
