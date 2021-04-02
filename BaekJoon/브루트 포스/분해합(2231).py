n = int(input())
m = 0
while True:
    m += 1
    s = str(m)
    r = list(map(str, s))
    l = len(r)
    fn = n
    for i in range(l):
        fn -= int(r[i])
    if fn == m :
        print(m)
        break
    if m >= n :
        print(0)
        break
    r = 0









"""
s = str(n)
r = list(map(str,s))
l = len(r)
"""