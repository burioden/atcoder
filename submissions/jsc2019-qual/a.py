m,d = map(int,input().split())

cnt = 0
for i in range(1,m+1):
  for j in range(1,d+1):
    if i == (j//10) * (j%10) and (j//10) >= 2 and (j%10) >= 2:
      cnt += 1
        
print(cnt)
