import sys

while True:
    j = 0
    stack = []
    str_data = sys.stdin.readline().rstrip()
    
    if str_data == '.':
        break
    
    for i in str_data:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(")")
        elif i == ']':
            if len(stack) != 0 and stack[-1] == '[':
                stack.pop()
            else:
                stack.append("]")
    if len(stack) == 0:
        print("yes")
    else:
        print("no")
        
