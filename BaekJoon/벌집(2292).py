n = int(input())
if n ==1:
    print(1)
    quit()
n = n-1
a = 1
while True:
    n = n -6*a
    if n <= 0:
        print(a+1)
        break
    a += 1