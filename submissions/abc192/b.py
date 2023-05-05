s = input()

flg = 1

for i in range(len(s)):
  if i%2 == 0:
    if 65 <= ord(s[i]) <= 96:
      flg = 0
      break
    else:
      continue
  else:
    if 97 <= ord(s[i]):
      flg = 0
      break

print('Yes' if flg else 'No')
