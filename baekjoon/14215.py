a, b, c = map(int,input().split())
    
while(True):
    if a + b <= c:
        c = c - 1
    elif b + c <= a:
        a = a - 1
    elif a + c <= b:
        b = b -1
    else:
        print(a+b+c)
        break

    
