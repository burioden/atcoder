import math
n = int(input())
s = input()

nya = []

cnt = 0
for i in range(1,n):
    if s[i-1] == s[i]:
        cnt += 1
    else:
        if cnt > 0:
            nya.append(cnt+1)
            cnt = 0

if cnt > 0:
    nya.append(cnt+1)

ans = 0
for i in nya:
    ans += math.comb(i,2)
    
print(ans)
