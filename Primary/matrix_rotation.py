# Enter your code here. Read input from STDIN. Print output to STDOUT
t=int(input())
for tc in range(t):
    n=int(input())
    print(f'Test Case #{tc+1}:')
    if n==1:
        ele=int(input())
        print(ele)
        continue
    l=[list(map(int,input().split())) for _ in range(n)]
    ans=[[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            ans[i][j]=l[n-1-j][i]

    for i in range(n):
        for j in range(n):
            print(ans[i][j],end=' ')
        print()