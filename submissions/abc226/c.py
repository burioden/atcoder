n = int(input())
w = []
t = []

for i in range(n):
  tt, k, *a = list(map(int, input().split()))
  t.append(tt)
  w.append(a)

# 必要なワザ  
need = set()

# 次の探索対象
neko = [n - 1]

while neko:
  p = neko.pop()
  need.add(p)
  
  for i in w[p]:
    if (i - 1) not in need:
      neko.append(i - 1)

ans = 0      
for i in need:
  ans += t[i]
  
print(ans)
