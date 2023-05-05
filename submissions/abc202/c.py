n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = list(map(int,input().split()))

# 全探索TLEの後に考えたこと
# 「例えば1,2のペアがOKなら、重複してる1,2のペアもOKになるなあ」
# 探し方がわからないなあ…考え方は合っていたぞ

cnt = [0]*(n+1)
ans = 0

# 各数字（iに該当）が何回使われてるかを格納していく
for i in a:
  cnt[i] += 1

# 固定できたi = cnt[i]を利用して、jの存在を手繰り寄せる
# ans には jが叶わない数字であれば0が足される
for j in range(n):
  ans += cnt[b[c[j]-1]]

print(ans)
