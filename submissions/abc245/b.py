n = int(input())
a = sorted(list(map(int,input().split())))

if len(set(a)) == 1:
  if a[0] == 0:
    print(1)
  else:
    print(0)
else:
  for i in range(2001):
    if i not in a:
      print(i)
      break
