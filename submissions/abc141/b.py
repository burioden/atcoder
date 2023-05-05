s = input()

flg = 1
for i,d in enumerate(s):
  if i%2 == 0:
    if d == "L":
      flg = 0
      break
  else:
    if d == "R":
      flg = 0
      break

print('Yes' if flg else 'No')
