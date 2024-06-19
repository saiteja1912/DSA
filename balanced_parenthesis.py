from stack import Stack
def is_match(c,top):
    if c=='}' and top=='{':
        return True
    elif c==')' and top=='(':
        return True
    elif c==']' and top=='[':
        return True
    else:
        return False
def is_paren_balanced(s):
    stack=Stack()
    i=0
    is_balanced=True
    while i<len(s) and is_balanced:
        if s[i] in '{[(':
            stack.push(s[i])
        elif stack.is_empty():
            is_balanced=False
        else:
            top=stack.pop()
            if not is_match(s[i],top):
                is_balanced=False
        i+=1
    
    if stack.is_empty() and is_balanced:
        return True
    else:
        return False
    

s=input("Enter string: ")
print(f's is {s}')
if(is_paren_balanced(s)):
    print(f'{s} is balanced')
else:
    print(f'{s} is not balanced')