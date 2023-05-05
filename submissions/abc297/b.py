s = list(input())

b = 0
ans = []

for i, d in enumerate(s):
  if d == 'B':
    b += i
  elif d == 'R' or d == 'K':
    ans.append(d)

print('Yes' if b % 2 == 1 and ans[1] == 'K' else 'No')
