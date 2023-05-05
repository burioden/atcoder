n = int(input())
s = input()

for i, d in enumerate(s):
  if d == '1':
    exit(print('Aoki' if i % 2 == 1 else 'Takahashi'))
