# Enter your code here. Read input from STDIN. Print output to STDOUT
def gcd_iterative(a,b):
    while(a>0 and b>0):
        if a>b:
            a=a%b
        else:
            b=b%a
    if a==0:
        return b
    return a



t=int(input())
for _ in range(t):
    n1,n2=map(int,input().split())
    hcf=gcd_iterative(n1,n2)
    lcm=(n1*n2)//hcf
    print(f'{lcm} {hcf}')