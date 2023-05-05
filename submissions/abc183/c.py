'''
とっても全探索
'''
import itertools

n, k = map(int, input().split())
time = []
num = []
for i in range(n):
  a = list(map(int, input().split()))
  time.append(a)
  num.append(i + 1)

num.pop()
num_li = itertools.permutations(num, n-1)

cnt = 0

for i in range(n):
  for j in num_li:
    x = 0
    for l in range(1,n - 1):
      x += (time[j[l - 1]][j[l]])
    x += time[0][j[0]] + time[j[n-2]][0]
    if x == k:
      cnt += 1
      
print(cnt)
