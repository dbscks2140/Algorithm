n = int(input())
k = 1

while True:
    n = n - k

    if n <= 0:
        if k%2 == 1:
           print(str(1-n)+"/"+str(k+n))
           break
        elif k%2 == 0:
            print(str(k+n)+"/"+str(1-n))
            break
    k += 1