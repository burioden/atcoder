n = int(input())
s = [input() for _ in range(n)]
m = int(input())
t = [input() for _ in range(m)]

w = list(set(s))

x = 0
for i in range(len(w)):
  x = max(x,s.count(w[i]) - t.count(w[i]))

print(max(0,x))
