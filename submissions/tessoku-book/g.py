d = int(input())
n = int(input())
a = [0]*(d+2)
for i in range(n):
  l,r = map(int,input().split())
  a[l] += 1
  a[r+1] -=1

# これ画期的すぎる
for i in range(1,d+1):
  a[i] += a[i-1]
  print(a[i])
