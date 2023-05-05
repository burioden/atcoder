a = int(input())
b = int(input())
n = int(input())

l = sorted([a,b])
ans = 0
i = 1

while ans <= n:
  if (l[1]*i)%l[0] == 0:
    ans = l[1]*i
    if ans == n:
      break
    i += 1
  else:
    i += 1

print(ans)
