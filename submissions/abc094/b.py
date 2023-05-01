n,m,x = map(int, input().split())
li = list(map(int, input().split()))

o = [0]*(n+1)
before = 0
after = 0

for i in li:
  o[i] += 1

for i in range(x):
  before += o[i]

for i in range(x,n+1):
  after += o[i]

print(min(before,after))
