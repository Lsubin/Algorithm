n = int(input())
stack = []
for i in range(n):
    number = int(input())
    if number == 0:
        stack.pop()
    else:
        stack.append(number)

print(sum(stack))
