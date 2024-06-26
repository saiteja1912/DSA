# Enter your code here. Read input from STDIN. Print output to STDOUT
t=int(input())
for tc in range(t):
    n=int(input())
    print(f'Case #{tc+1}:')
    for i in range(0,n):
        for j in range(0,n):
            if((i==0 and j==n//2) or (j==0 and i==n//2) or (i==n-1 and j==n//2) or (j==n-1 and i==n//2)):
                print('*',end='')
            elif(j==n//2+i or i+j==n//2 or i==n//2+j) or j==(n//2)+(n-1-i):
                print('*',end='')
            else:
                print(' ',end='')

            # if(i<n//2):
            #     #upper part of diamond including middle line
            #     if j==n//2-i or j==n//2+i:
            #         print('*',end='')
            #     else:
            #         print(' ',end='')
            # else:
            #     #lower part of diamond
            #     if j==i-n//2 or j==(n//2)+(n-1-i):
            #         print('*',end='')
            #     else:
            #         print(' ',end='')
        print()

    
