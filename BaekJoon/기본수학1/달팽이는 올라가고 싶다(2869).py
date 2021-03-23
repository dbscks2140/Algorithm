import math
a, b, v  = map(int,input().split())
if (v-a) % (a-b) == 0:
    print(int((v - a) / (a - b) + 1))
else:
    print(int((v-a) / (a-b)+2))



"""
while True:
    v = v - a
    if v <= 0 :
        print(d)
        break
    v = v + b
    d += 1
"""