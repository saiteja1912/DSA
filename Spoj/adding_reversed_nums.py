def reverse(n):
    ans=0
    while(n!=0):
        rem=n%10
        ans=ans*10+rem
        n=n//10
    return ans

n=int(input())
for t in range(n):
    a,b=map(int,input().split())
    print(reverse(reverse(a)+reverse(b)))