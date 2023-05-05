s = list(input())

ans = 9999
for i in range(len(s)-2):
  x = abs(753 - int(s[i]+s[i+1]+s[i+2]))
  ans = min(x,ans)

print(ans)
