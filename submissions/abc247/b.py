n = int(input())
name = [input().split() for _ in range(n)]

import collections

c = collections.Counter()

for i, d in name:
  c[i] += 1
  c[d] += 1
  
for i, d in name:
  if i == d: # 名字と名前が一緒の場合
    if c[i] <= 2 or c[d] <= 2: # 他で使われてるか判定(他で使われてたら3以上になる)
      continue
    else:
      print('No')
      exit()
  elif c[i] >= 2 and c[d] >= 2:
    print('No')
    exit()

print('Yes')
