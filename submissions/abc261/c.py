n = int(input())
a = {}
for i in range(n):
  s = input()
  if s in a:
    print(s + "(" + str(a[s]) + ")")
    a[s] += 1
  else:
    print(s)
    a[s] = 1
