# cook your dish here
t=int(input())
for _ in range(t):
    n,x,y=map(int,input().split())
    max_2hr_sessions=n//2
    max_1hr_sessions=n
    if n%2==1:
        print(max(max_2hr_sessions*y+x,max_1hr_sessions*x))
    else:
        print(max(max_2hr_sessions*y,max_1hr_sessions*x))