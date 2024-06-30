# Enter your code here. Read input from STDIN. Print output to STDOUT
t=int(input())
for _ in range(t):
    n=int(input())
    l=[list(map(int,input().split())) for _ in range(n)]
    c=n-1
    for k in range(n):
        sum=0
        for i in range(n):
            for j in range(n-1,i-1,-1):
                if j-i == c:
                    #print(l[i][j],end=' ')
                    sum+=l[i][j]
        print(sum,end=' ')
        c-=1

    c=1
    for k in range(n):
        sum=0
        for i in range(n-1,0,-1):
            for j in range(i):
                if i-j == c:
                    #print(l[i][j],end=' ')
                    sum+=l[i][j]
        if k!=n-1:
            print(sum,end=' ')
        c+=1
    print()
    #print(f'\ntest case over')