n = int(input())
distances = list(map(int,input().split()))
oil = list(map(int, input().split()))

total_prices = 0

c = oil[0]

for i in range(n-1):
    if c > oil[i]:
        c = oil[i]
    total_prices += c * distances[i]

print(total_prices)
