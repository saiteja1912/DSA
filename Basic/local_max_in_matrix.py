# Enter your code here. Read input from STDIN. Print output to STDOUT
def local_max_matrix(l,n):
    a=[[-1001]*(n-2) for _ in range(n-2)]
    p,q=0,0
    for i in range(1,n-1):
        q=0
        for j in range(1,n-1):
            a[p][q]=max(l[i-1][j-1],l[i-1][j],l[i-1][j+1],l[i][j-1],l[i][j],l[i][j+1],l[i+1][j-1],l[i+1][j],l[i+1][j+1])
            q+=1
        p+=1
    return a

n=int(input())
l=[list(map(int,input().split())) for _ in range(n)]
l=local_max_matrix(l,n)
for r in l:
    print(*r)
