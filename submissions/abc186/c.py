n = int(input())

cnt = 0
for i in range(1,n+1):
  if '7' in str(i) or '7' in str(oct(i)):
    cnt += 1
    
print(n-cnt)
