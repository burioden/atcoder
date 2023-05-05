n = int(input())
a = [int(input()) for _ in range(n)]

b = sorted(set(a),reverse=True)

ma = b[0]
if len(b) > 1:
  mi = b[1]
else:
  mi = b[0]

c = a.count(ma)

if c > 1:
  for i in range(n):
    print(ma)
else:
  for i in a:
    if i != ma:
      print(ma)
    else:
      print(mi)
