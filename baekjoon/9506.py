while(True):
    divisor = []
    n = int(input())
    for i in range(1,n):
        if n % i == 0:
            divisor.append(i)
    if n == -1:
        break
    elif sum(divisor) == n:
        print(f"{n} = " + " + ".join(map(str,divisor)))
    else:
        print(f"{n} is NOT perfect.")
    
