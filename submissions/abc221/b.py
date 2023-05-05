s = list(input())
t = list(input())

flg = 0

if s == t:
  flg = 1
else:
  for i in range(len(s)-1):
    s[i],s[i+1] = s[i+1],s[i]
    if s == t:
      flg = 1
    s[i],s[i+1] = s[i+1],s[i]

print('Yes' if flg else 'No')
