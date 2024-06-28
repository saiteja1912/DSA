# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
for i in range(n):
    for j in range(i+1):
        print(j+1,end=' ')
    print()
n=n-1
for i in range(n,0,-1):
    for j in range(i):
        print(j+1,end=' ')
    print()