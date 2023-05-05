n,k = map(int,input().split())
a = list(map(int,input().split()))

import collections

c = collections.Counter(a)
m = len(c)
l = c.most_common()[::-1]

cnt = 0
for i,d in l:
  if m > k:
    m -= 1
    cnt += d
  else:
    break
  
print(cnt)
