# Enter your code here. Read input from STDIN. Print output to STDOUT
n,m=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(n)]
b=[list(map(int,input().split())) for _ in range(n)]
l=[[0 for _ in range(m)] for _ in range(n)]
for i in range(n):
    for j in range(m):
        l[i][j]=a[i][j]+b[i][j]

for i in range(n):
    for j in range(m):
        print(l[i][j],end=' ')
    print()