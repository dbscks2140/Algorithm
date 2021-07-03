n = int(input())
da = [' 'for _ in range(n)]
count = [0 for _ in range(10001)]
f = [0 for _ in range(n-1)]
for i in range(n):       # 입력
    da[i] = int(input())

for i in range(n):      #수의 개수 저장
    count[da[i]] += 1
for i in range(10000):
    count[i] += count[i-1]

for i in range(n-1,0,-1):
    s = count[da[i]]
    s -= 1
    f[s-1] = da[i]
print(f)
