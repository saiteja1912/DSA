# Enter your code here. Read input from STDIN. Print output to STDOUT
n,m=map(int,input().split())
l=[list(map(int,input().split())) for _ in range(n)]
t=[[0 for _ in range(n)] for _ in range(m) ]
for i in range(n):
    for j in range(m):
        t[j][i]=l[i][j]

for i in range(m):
    for j in range(n):
        print(t[i][j],end=' ')
    print()