n = int(input())
a = sorted(list(map(int,input().split())))[::-1]

alice = 0
bob = 0

for i in range(n):
  if i%2 == 0:
    alice += a[i]
  else:
    bob += a[i]

print(abs(alice-bob))
