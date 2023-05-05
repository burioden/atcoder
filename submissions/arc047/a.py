n,l = map(int,input().split())
s = input()

cnt = 1
ans = 0
for i,d in enumerate(s):
  if d == '+':
    cnt += 1
    if cnt == l+1:
      ans += 1
      cnt = 1
  elif d == '-':
    cnt -= 1
    
print(ans)
