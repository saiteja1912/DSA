# Enter your code here. Read input from STDIN. Print output to STDOUT
t=int(input())
for _ in range(t):
    zeros=0
    n=int(input())
    while(n//5>0):
        zeros+=n//5
        n=n//5
    print(zeros)