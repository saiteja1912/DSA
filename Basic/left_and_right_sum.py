# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
l=list(map(int,input().split()))
ts=0
for i in l:
    ts+=i
rs=[0]*n
ls=[0]*n

#calc left sum of each ele
rs[0]=ts-l[0]
for i in range(1,n):
    rs[i]=rs[i-1]-l[i]

ls[n-1]=ts-l[-1]
for i in range(n-2,-1,-1):
    ls[i]=ls[i+1]-l[i]

for i in range(n):
    if ls[i]>rs[i]:
        print(ls[i]-rs[i],end=' ')
    else:
        print(rs[i]-ls[i],end=' ')