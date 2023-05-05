import collections

n = int(input())
li = [input() for i in range(n)]

li_c = collections.Counter(li)
m = li_c.most_common()[0][1]
k = [i for i,v in li_c.items() if v == m]
k.sort()

for i in range(len(k)):
  print(k[i])
