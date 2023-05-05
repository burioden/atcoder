a = list(map(int, input().split()))

for i, d in enumerate(a):
  if d == 0:
    print(i + 1)
