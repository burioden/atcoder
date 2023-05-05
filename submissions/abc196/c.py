n = input()

a = len(n)
ans = 0

if a%2 == 1:
  x = n[:a//2+1]
  b = n[a//2+1:]
else:
  x = n[:a//2]
  b = n[a//2:]

if a==1:
  ans = 0
elif a%2 == 1:
    ans = "9"*(a//2)
elif a%2 == 0:
  if int(x) <= int(b):
    ans = x
  else:
    ans = int(x)-1

print(ans)
