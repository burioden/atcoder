s = input()

ans = s.count('R')

if ans == 2:
  if s[0] == s[2] and s[0] != s[1]:
    ans = 1
    
print(ans)
