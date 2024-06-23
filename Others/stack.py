"""
Implemetation of stack
"""
class Stack:
    def __init__(self):
        self.items=[]

    def is_empty(self):
        return self.items == []
    
    def push(self,item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        print('Stack is empty')
            
    def stack_length(self):
        return len(self.items)
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        print('Stack is empty')

    def get_stack(self):
        return self.items
    
stack=Stack()
stack.push('213')
stack.push('abc')
print(stack.get_stack())
print(stack.items)
# print(f's is pop: {stack.pop()}')
# print(stack.get_stack())
# print(stack.stack_length())
# print(stack.peek())

abc=[1]
print(abc.pop())