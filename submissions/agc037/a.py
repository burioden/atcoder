s = input()
cnt = len(s)

i = 0

while i < len(s)-1:
  if s[i]==s[i+1]:
    cnt -= 1
    i += 3
  else:
    i += 1

print(cnt)
