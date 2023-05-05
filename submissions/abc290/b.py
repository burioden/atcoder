n, k = map(int, input().split())
s = list(input())

cnt = 0
for i, d in enumerate(s):
  if d == 'o' and cnt < k:
    cnt += 1
  elif d == 'o' and cnt >= k:
    s[i] = 'x'
    
print(*s,sep='')
