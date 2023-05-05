import collections

n = int(input())
li = [input() for _ in range(n)]

li_c = collections.Counter(li)
print(li_c.most_common()[0][0])
