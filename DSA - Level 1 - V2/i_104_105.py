#DUPLICATE BRACKETS
'''
1) exp='((a+b)+(c+d))' - False
2) exp='(a+b)+(((c))+d)' - True

'''

def checkForDuplicateBrackets(exp):
    stack=[]
    i=0
    for i in range(len(exp)):
        if exp[i]==')':
            #if element is ) check if there is some content inside this bracket

            if len(stack)>0 and stack[-1]=='(':
                #if there is no content withinand directly ( is found then there is a duplicacy
                return True
            while len(stack)>0 and stack[-1]!='(':
                #Remove all the content within and pop the opening bracket as well
                stack.pop()
            stack.pop()
        else:
           #if element is anything other than ), push itz
           stack.append(exp[i])
    return False

if __name__ == '__main__':
    exp='((a+b)+(c+d))'
    result=checkForDuplicateBrackets(exp)
    print(result)
    exp='(a+b)+(((c))+d)'
    result=checkForDuplicateBrackets(exp)
    print(result)