n,m = map(int,input().split())
solve = [input().split() for _ in range(m)]

a = set()
p = [0] * n
w = 0

for i,d in solve:
  if i in a:
    continue
  elif d == "AC":
    a.add(i)
    w += p[int(i)-1]
  else:
    p[int(i)-1] += 1

print(len(a),w)
