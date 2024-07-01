n = int(input())

data = []
endpoint = 0
result = 0

for i in range(n):
    a, b = map(int,input().split())
    data.append([a, b])

data.sort(key=lambda x: (x[1],x[0]))

for start, end in data:
    if endpoint <= start:
        result += 1
        endpoint = end
print(result)
