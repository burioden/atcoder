x = list(map(int,input()))
a = x[0]
b = x[1]
c = x[2]
d = x[3]

ans = "Strong"

if len(set(x))==1:
  ans = "Weak"
elif ((a+1)%10==b%10) and ((b+1)%10==c%10) and ((c+1)%10==d%10):
  ans = "Weak"

print(ans)
