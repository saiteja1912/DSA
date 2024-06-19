from stack import Stack
def binary(n):
    # s=''
    # while n>0:
    #     s=str(n%2)+s
    #     n//=2
    # return s
        
    #approach 2 using stack
    stack=Stack()
    while n>0:
        stack.push(n%2)
        n//=2
    s=''
    while not stack.is_empty():
        s+=str(stack.pop())
    return s
    

n=int(input("enter decimal number: "))
print(f'binary representation of {n} is {binary(n)}')
print(int(binary(56),2)==56) #1011 -> 2^0*1 + 2^1*1 + 2^2*0 + 2^3*1

print(int('11',3)) #4
