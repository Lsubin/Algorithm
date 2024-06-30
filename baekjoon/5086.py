answer = []

while(True):
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    elif b % a == 0:
        answer.append('factor')
    elif a % b == 0:
        answer.append('multiple')
    else:
        answer.append('neither')

for i in range(len(answer)):
    print(answer[i])
