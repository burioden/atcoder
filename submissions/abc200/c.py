n = int(input())
a = list(map(int,input().split()))

cnt = [0]*202

# iを保管しながら、条件に合うjを探してansに足す
ans = 0
for i in range(n):
  x = a[i]%200
  ans += cnt[x]
  cnt[x] += 1
  
print(ans)
