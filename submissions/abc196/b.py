s = input()
li = list(s)
if "." in li:
  x = max(-1,li.index("."))
else:
  x = 0

print(''.join(map(str, li[:x])) if x > 0 else s)
