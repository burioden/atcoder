a, b, c = map(int, input().split())

if a > b:
  print('Takahashi')
elif a < b:
  print('Aoki')
else:
  if c == 1:
    print('Takahashi')
  else:
    print('Aoki')
