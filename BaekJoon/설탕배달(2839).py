n = int(input())
k = 0
while True:
    if n%5 == 0:
        k = k + (n//5)
        print(k)
        break
    n = n-3
    k += 1
    if n < 0:
        print(-1)
        break

