n = int(input())
a = list(map(int,input().split()))

s = sum(a)
cnt = 0
if s % n != 0:
  cnt = -1
elif len(set(a)) == 1:
  cnt = 0
else:
  m = 0
  for i in a:
    m += i - s//n
    if m != 0:
      cnt += 1
      
print(cnt)
