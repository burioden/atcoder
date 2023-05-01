n = int(input())

if n==1:
  ans = 1
elif n%2==1:
  ans = (n//2+1)/n
else:
  ans = (n//2)/n

print(ans)
