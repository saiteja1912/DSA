# cook your dish here
t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    l.sort()
    array_exist=True
    for i in range(len(l)):
        if l[i]>i+1:
            array_exist=False
            break
    if array_exist==False:
        print('NO')
    else:
        print('YES')