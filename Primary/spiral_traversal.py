# Enter your code here. Read input from STDIN. Print output to STDOUT
def print_spiral(l,n):
    left=0
    top=0
    right=n-1
    bottom=n-1

    while(left<=right and top<=bottom):
        #left to right
        for i in range(left,right+1):
            print(l[top][i],end=' ')
        top+=1

        #top to bottom
        for i in range(top,bottom+1):
            print(l[i][right],end=' ')
        right-=1

        #right to left
        if top<=bottom: #to ignore printing again when there is only 1 row
            for i in range(right,left-1,-1):
                print(l[bottom][i],end=' ')
            bottom-=1

        #bottom to top
        if left<=right: #to ignore printing again when there is only 1 column
            for i in range(bottom,top-1,-1):
                print(l[i][left],end=' ')
            left+=1
    print()
        


t=int(input())
for _ in range(t):
    n=int(input())
    l=[list(map(int,input().split())) for _ in range(n)]
    print_spiral(l,n)