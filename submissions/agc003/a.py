s = input()
S = sorted(set(s))
n = len(S)

if n == 4:
  print('Yes')
elif n == 2:
  if S == ["N","S"]:
    print('Yes')
  elif S == ["E","W"]:
    print('Yes')
  else:
    print('No')
else:
  print('No')
