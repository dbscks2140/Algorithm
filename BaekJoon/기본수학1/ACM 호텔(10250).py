t = int(input())
for i in range(t):
    h, w, n = map(int, input().split())
    x = str(n%h)
    if(n%h == 0):
        x = str(h)
        y = n//h
        k = format(y, '02')
        print(x + k)
        continue
    y = n//h + 1
    k = format(y, '02')
    print(x+k)