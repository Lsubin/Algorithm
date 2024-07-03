import sys
from collections import deque

queue = deque()

n = int(sys.stdin.readline().strip())

for i in range(n):
    cmd = sys.stdin.readline().strip().split()

    if cmd[0] == 'push':
        queue.append(cmd[1])
    elif cmd[0] == 'pop':
        if queue:
            print(queue.popleft())        
        else:
            print(-1)
    elif cmd[0] == 'size':
        print(len(queue))
    elif cmd[0] == 'empty':
        if not queue:
            print(1)
        else:
            print(0)
    elif cmd[0] == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif cmd[0] == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)
