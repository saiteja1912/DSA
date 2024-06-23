n=int(input())
for t in range(n):
    s=input()
    if(len(s)<=10):
        print(s)
    else:
        print(s[0]+str(len(s)-2)+s[-1])
        #print(st[0], l - 2, st[l - 1], sep='')