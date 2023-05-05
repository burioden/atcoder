n,x = map(int,input().split())
a = list(map(int,input().split()))

ans = 0

for i in range(n):
  # xをi回右シフト（2進数に変換）し、2進数にしたx[i]に1のフラグが立ってるか
  if (x>>i) & 1:
    ans += a[i]

print(ans)
