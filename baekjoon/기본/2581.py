M = int(input())
N = int(input())

number = list(range(M,N+1))
prime_number = []

for item in number:
    count = 0
    for i in range(1,item+1):
        if item % i == 0:
            count += 1
    if count == 2:
        prime_number.append(item)

if len(prime_number) > 0:
    print(sum(prime_number))
    print(prime_number[0])
else:
    print("-1")
