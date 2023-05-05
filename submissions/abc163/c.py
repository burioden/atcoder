n = int(input())
a = list(map(int,input().split()))

s = [0]*n

for i in a:
  s[i-1] += 1
  
for i in s:
  print(i)
