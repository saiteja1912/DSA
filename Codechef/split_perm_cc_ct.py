# cook your dish here
t = int(input())
for i in range(t):
    n = int(input())
    l = []
    if n%2 == 0:
        max_ = n+ 1 
        for i in range(1,n//2+1):
            l.append(i)
            l.append(max_-i)
    else:
        max_ = n
        for i in range(1,n//2+1):
            l.append(i)
            l.append(max_ - i)
        l.append(n)
    for i in l:
        print(i,end=" ")
    print()