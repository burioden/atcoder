n = int(input())
a = list(map(int, input().split()))

yonda = set()

for i, d in enumerate(a):
  if i + 1 not in yonda:
    yonda.add(d)

print(n - len(yonda))
for i in range(n):
  if i + 1 not in yonda:
    print(i + 1, end=' ')
