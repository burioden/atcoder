n = int(input())
s = input()
t = input()

if s==t:
  print(n)
  exit()

S = []
T = []

for i in range(1,n+1):
  S.append(s[n-i:n])
  T.append(t[0:i])

ans = 0
for i in range(n):
  if S[i] == T[i]:
    ans = (n*2) - (i+1)
    break
else:
  ans = n*2

print(ans)
