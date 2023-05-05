import collections

n = int(input())
a = list(map(int, input().split()))

c = collections.Counter(a)

cnt = 0
for i, d in c.items():
  cnt += (d // 2)
    
print(cnt)
