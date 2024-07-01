n = int(input())

plans = list(input().split())

# 동, 북, 서, 남
dx = [0, -1, 0, 1]
dy = [1, 0 , -1, 0] 

move_types = ['R','U','L','D']

# 현재 위치
x, y = 1, 1

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny

print(x, y)
