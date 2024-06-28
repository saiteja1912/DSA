# Enter your code here. Read input from STDIN. Print output to STDOUT
c,r=map(int,input().split())
for i in range(r):
    for j in range(c):
        if i==0 or j==0 or i==r-1 or j==c-1:
            print('*',end='')
        else:
            print(' ',end='')
    print()