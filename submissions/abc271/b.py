n,q = map(int,input().split())
a = [list(map(int, input().split())) for _ in range(n)]
s = [list(map(int, input().split())) for _ in range(q)]

for i in range(q):
  print(a[s[i][0]-1][s[i][1]])
