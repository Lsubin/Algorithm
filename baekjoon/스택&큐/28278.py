import sys

n = int(sys.stdin.readline().strip())
    
stack = []

for i in range(n):
    command = list(map(int,sys.stdin.readline().strip().split()))
    if command[0] == 1:
        stack.append(int(command[1]))
    elif command[0] == 2:   
        if len(stack) != 0:
            print(stack.pop())
        else:
            print(-1)
    elif command[0] == 3:
        print(len(stack))
    elif command[0] == 4:
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == 5:
        if len(stack) != 0:
            print(stack[-1])
        else:
            print(-1)

