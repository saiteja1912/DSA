# cook your dish here
t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    cd=list(map(int,input().split()))
    cc=list(map(int,input().split()))
    d1=dict()
    d2=dict()
    for i in cd:
        r=i%m
        if r in d1:
            d1[r]+=1
        else:
            d1[r]=1
    
    for i in cc:
        r=i%m
        if r in d2:
            d2[r]+=1
        else:
            d2[r]=1
    if 0 in d1 and 0 in d2:
        ways=d1[0]*d2[0]
    else:
        ways=0
    #print(d1)
    #print(d2)
    for i in range(1,m):
        if i in d1 and m-i in d2:
            ways+=d1[i]*d2[m-i]
    print(ways)
        