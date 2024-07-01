n = int(input())
data = list(map(int, input().split()))

data.sort()

result = 0

for i in range(n):
    time = 0
    for j in range(n-i):
        time += data[j]
    result += time
print(result)
