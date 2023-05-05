n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

acnt = 0
bcnt = len(set(a) & set(b))
if bcnt < 0:
  bcnt = 0

for i in range(n):
  if a[i] == b[i]:
    acnt += 1
    bcnt -= 1

print(acnt)
print(bcnt)


