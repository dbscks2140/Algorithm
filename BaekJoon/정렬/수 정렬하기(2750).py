import sys
n = int(sys.stdin.readline())
t = [' 'for _ in range(n)]
for i in range(n):
    t[i] = int(sys.stdin.readline())
t.sort(reverse=False)
for i in t:
    print(i, end= '')
    print()
