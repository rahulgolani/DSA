def checkIfBalanced(exp):
    stack=[]
    for char in exp:
        if char=='(' or char=='{' or char=='[':
            stack.append(char)
        
        elif char==')' or char=='}' or char==']':
            if len(stack)==0:
                # Multiple closing brackets
                return False
            elif char==')' and stack[-1]=='(':
                stack.pop()
            elif char=='}' and stack[-1]=='{':
                stack.pop()
            elif char==']' and stack[-1]=='[':
                stack.pop()
            else:
                return False
        
    if len(stack)>0:
        # If there are multiple opening brackets
        return False
    return True

if __name__ == '__main__':
    exp='[(a+b)+{(c+d)*(e/f)}]'
    print(checkIfBalanced(exp))