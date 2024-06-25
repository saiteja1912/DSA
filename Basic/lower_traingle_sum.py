# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
l=[list(map(int,input().split())) for _ in range(n)]
sum=0
for i in range(n):
    for j in range(n):
        if i>=j:
            sum+=l[i][j]

print(sum)