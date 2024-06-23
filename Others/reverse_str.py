from stack import Stack

def reverse(str):
    #approach 1
    #return str[::-1]

    #approach 2
    # stack=Stack()
    # i=0
    # while i<len(str):
    #     stack.push(str[i])
    #     i+=1
    # rev_str=''
    # print(f'stack is {stack.get_stack()}')
    # print(f'len of stack is {stack.stack_length()}')
    # i=0
    # while i<len(str):
    #     rev_str+=stack.pop()
    #     i+=1
    # return rev_str

    #optimal approach 3
    stack=Stack()
    for i in range(len(str)):
        stack.push(str[i])
    rev_str = ""
    while not stack.is_empty():
        rev_str += stack.pop()
    return rev_str



# s=input('enter string: ')
# rev_s=reverse(s)
# print(f'reverse of {s} is {rev_s}')