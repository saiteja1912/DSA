# Enter your code here. Read input from STDIN. Print output to STDOUT
def bin_search(a,n,k):
    l=0
    h=n-1
    while(l<=h):
        m=(l+h)//2
        print(str(l)+' '+str(h)+' '+str(m))
        if a[m]<k:
            l=m+1
        elif a[m]>k:
            h=m-1
        else:
            return True
    return False


n,k=map(int,input().split())
a=list(map(int,input().split()))
print(bin_search(a,n,k))


