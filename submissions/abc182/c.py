s = list(map(int,input()))
n = len(s)

# %3 == 1を入れる
a = []
# %3 == 2を入れる
b = []

for i in s:
  if i % 3 == 1:
    a.append(i)
  elif i % 3 == 2:
    b.append(i)

A = len(a)
B = len(b)

if A == n or B == n:
  print(-1)
  exit()
elif A == B:
  print(0)
  exit()

print(min(abs(A-B),abs((A%3)-(B%3))))
