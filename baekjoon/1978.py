n = int(input())

answer = list(map(int,input().split()))

prime_count = 0

for num in answer:
    count = 0
    for i in range(1,num+1):
        if num % i == 0:
            count += 1
    if count == 2:
        prime_count += 1

print(prime_count)
                
