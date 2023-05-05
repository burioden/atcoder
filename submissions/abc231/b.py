import collections
n = int(input())
li = []
for i in range(n):
  s = input()
  li.append(s)

li_c = collections.Counter(li)
print(li_c.most_common()[0][0])
