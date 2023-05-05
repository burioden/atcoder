s = input()

n = len(s)

flg = 1

for i in range(n):
    if s[i] != s[(n-1)-i]:
        flg = 0

if s[0:(n-1)//2] == s[((n+3)//2)-1:n] and flg:
  print('Yes')
else:
  print('No')
