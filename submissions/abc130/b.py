n,x = map(int,input().split())
l = list(map(int,input().split()))
sum_l = l[:]

for i in range(1, n):
    sum_l[i] += sum_l[i-1]

cnt = 1
for i in sum_l:
  if i <= x:
    cnt += 1

print(cnt)
