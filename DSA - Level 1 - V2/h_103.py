#INTRODUCTION TO STACKS

'''
Operations->
1) Push
2) Pop
3) Peek
4) Display
'''

class Stack:
    def __init__(self) -> None:
        self.stack=[]
    
    def push(self,data):
        self.stack.append(data)
    
    def pop(self):
        if len(self.stack)==0:
            print('Stack Empty')
            return
        return self.stack.pop()
    
    def peek(self):
        if len(self.stack)==0:
            print('Stack Empty')
            return
        print(self.stack[-1])
    
    def display(self):
        if len(self.stack)==0:
            print('Stack Empty')
            return
        top=len(self.stack)-1
        while top>=0:
            if top==0:
                print(self.stack[top],end='')
            else:
                print(self.stack[top],end='->')
            top-=1
        print()


if __name__ == '__main__':
    stack=Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.display()
    stack.peek()
    stack.pop()
    stack.peek()
    stack.pop()
    stack.peek()
    stack.display()
    stack.pop()
    stack.pop()
    stack.pop()
    stack.pop()
    stack.display()