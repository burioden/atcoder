n = int(input())
a = [int(input()) for _ in range(n)]

import collections

c = collections.Counter(a)

import collections

c = collections.Counter(a)

cnt = 0
for i,d in c.items():
  if d%2 == 1:
    cnt += 1
    
print(cnt)
