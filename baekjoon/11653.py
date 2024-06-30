num = int(input())

i = 2

while(True):
    if num == 1:
        break
    elif num % i == 0:
        num = num / i
        print(i)
    else:
        i += 1
   
