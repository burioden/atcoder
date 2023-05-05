n = int(input())
a = sorted(list(map(int,input().split())),reverse=True)

l = len(set(a))
if l == 1:
  print(n)
  if 1 < n:
    for i in range(n-1):
      print(0)
  exit()

cnt = 1
i = 0
j = 1
while i < n:
  if j == n:
    print(cnt)
    break
  if a[i] == a[j]:
    cnt += 1
    i += 1
    j += 1
  else:
    print(cnt)
    cnt = 1
    i += 1
    j += 1

for i in range(n-l):
  print(0)
