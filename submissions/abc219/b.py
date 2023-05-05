li = [input() for _ in range(3)]
t = list(map(int,input()))
ans = ""

for i in range(len(t)):
  ans += li[t[i]-1]

print(ans)
