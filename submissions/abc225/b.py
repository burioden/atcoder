import collections

n = int(input())
li = []
for i in range(n-1):
  a,b = map(int,input().split())
  li.append(a)
  li.append(b)

li_c = collections.Counter(li)

if li_c.most_common()[0][1] == n-1:
  print('Yes')
else:
  print('No')
