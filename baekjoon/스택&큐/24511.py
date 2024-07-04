import sys
from collections import deque

queuestack = deque()

n = int(sys.stdin.readline().rstrip())
list_a = list(map(int, sys.stdin.readline().rstrip().split()))
list_b = list(map(int, sys.stdin.readline().rstrip().split()))
m = int(sys.stdin.readline().rstrip())
list_c = list(map(int, sys.stdin.readline().rstrip().split()))

for i in range(n):
    if list_a[i] == 0:
        queuestack.append(list_b[i])

for j in range(m):
    queuestack.appendleft(list_c[j])

for k in range(m):
    print(queuestack.pop(), end=' ')




    
