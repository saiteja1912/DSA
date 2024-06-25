# Enter your code here. Read input from STDIN. Print output to STDOUT
n,m=map(int,input().split())
l=[list(map(int,input().split())) for _ in range(n)]
for i in range(m):
    sum=0
    for j in range(n):
        sum+=l[j][i]
    print(sum)
