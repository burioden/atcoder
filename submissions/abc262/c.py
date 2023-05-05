n = int(input())
a = list(map(int,input().split()))

# i+1 == dのもの
c1 = 0
# i+1 == a[d-1]のもの
c2 = 0

for i,d in enumerate(a):
  if i+1 == d:
    c1 += 1
  elif i+1 == a[d-1]:
    c2 += 1

s = 0
if c1 >= 2:
  s = (c1)*(c1-1)//2

print((c2//2)+s)
