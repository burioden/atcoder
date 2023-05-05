n,x = map(int,input().split())
s = input()

ans = x
for i in s:
  if i == 'o':
    ans += 1
  elif i == 'x':
      if ans == 0:
        continue
      else:
        ans -= 1
        
print(ans)
