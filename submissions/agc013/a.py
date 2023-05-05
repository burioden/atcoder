n = int(input())
a = list(map(int,input().split()))

# POINT！負と負はかけると+に、正と正もかけると+になることを利用！
# 符号を管理しながら、次のものとの差を見ていく
# 差と符号管理のものを掛け合わせて負になったら、そこが切り替えどころ

# 最小（どこでも区切らなくていいカタマリ1つだから）
ans = 1
# 符号を管理してくれる
c = 0

for i in range(n-1):
  sa = a[i+1] - a[i]
  if sa*c < 0:
    ans += 1
    c = 0
  elif c == 0:
    c = sa
    
print(ans)
