# Enter your code here. Read input from STDIN. Print output to STDOUT
def image_flip(l,n,m):
    for row in l:
        #print(f'row={row}')
        for i in range((m+1)//2):
            #print(f'before swap: row[{i}]={row[i]},row[{m-1-i}]={row[m-1-i]}')
            row[i],row[m-1-i]=row[m-1-i],row[i]
            #print(f'after swap: row[{i}]={row[i]},row[{m-1-i}]={row[m-1-i]}')
            row[i],row[m-1-i]=row[i]^1,row[m-i-1]^1
            #print(f'after xor: row[{i}]={row[i]},row[{m-1-i}]={row[m-1-i]}')
    return l

n,m=map(int,input().split())
l=[list(map(int,input().split())) for _ in range(n)]
l=image_flip(l,n,m)
for row in l:
    print(*row)