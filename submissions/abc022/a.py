n,s,t = map(int, input().split())
w = int(input())

li = []

if s <= w and w <= t:
  li.append(w)

for i in range(n-1):
  a = int(input())
  w += a
  if s <= w and w <= t:
    li.append(w)

print(len(li))
