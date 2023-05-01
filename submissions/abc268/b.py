s = input()
t = input()

flag = 1

if len(t) < len(s):
  flag = 0 
else:
  for i in range(len(s)):
    if s[i] != t[i]:
      flag = 0

print("Yes" if flag else "No")
