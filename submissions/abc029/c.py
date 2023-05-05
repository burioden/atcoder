import itertools

n = int(input())

# 重複アリで順列を作る時はproduct
s = list(itertools.product('abc',repeat=n))
s.sort()
for i in s:
  print(*i,sep="")
