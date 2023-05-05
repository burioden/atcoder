from itertools import combinations
n,m = map(int,input().split())
a = [i for i in range(1,m+1)]

for i in combinations(a,n):
  print(*i)
