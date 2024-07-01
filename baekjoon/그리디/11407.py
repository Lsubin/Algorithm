N, K = map(int,input().split())

coins = []
result = 0

for i in range(N):
    coins.append(int(input()))

for coin in coins[::-1]:
    if K >= coin:
        result += K // coin
        K = K % coin
print(result)
