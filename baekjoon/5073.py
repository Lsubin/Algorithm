while(True):
    length = list(map(int,input().split()))
    if length[0] == 0 and length[1] == 0 and length[2] == 0:
        break
    sorted(length)
    if length[0] + length[1] > length[2]:
        new_lenght = list(set(length))
        if len(new_lenght) == 2:
            print("Isosceles")
        elif len(new_lenght) == 1:
            print("Equilateral")
        else:
            print("Scalene")
    else:
        print("Invalid")
