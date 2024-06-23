n=int(input())
ans=0
for t in range(n):
    stmt=input()
    if("++" in stmt):
        ans+=1
    else:
        ans-=1
print(ans)