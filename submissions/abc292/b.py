n, q = map(int, input().split())
card = [0 for _ in range(n)]

for i in range(q):
  a, b = map(int, input().split())
  if a == 1:
    card[b - 1] += 1
  elif a == 2:
    card[b - 1] += 2
  elif a == 3:
    print('Yes' if card[b - 1] >= 2 else 'No')
