n = input()

pon = [0, 1, 6, 8]

m = int(n[-1])

if m in pon:
  print('pon')
elif m == 3:
  print('bon')
else:
  print('hon')
