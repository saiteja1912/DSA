while(True):
    a,b,c=map(int,input().split())
    if(a==0 and b==0 and c==0):
        break
    ans=''
    if(b-a==c-b):
        ans+="AP"
        next_ele=c+(b-a)
    elif(b/a==c/b):
        ans+="GP"
        next_ele=c*(b//a)
    ans=ans+" "+str(next_ele)
    print(ans)