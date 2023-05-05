s = input()
n = len(s)
k ="keyence"

flg = 1

# はじめて違う文字を見つけたら、マイナスインデックスで後ろからも同時に見ていく（かしこい…）
for i in range(7):
  if s[i] != k[i]:
    if s[-7+i] != k[-7+i]:
      flg = 0
      break

print('YES' if flg else 'NO')

# -- ダメだったコード -- 
# OKなパターンは3つ
# 1.keyencexxx
# 2.xxxkeyence
# 3.keyxxxence など、頭とお尻に分かれてるパターン
# 分かれてるパターンに関して、はじめて違った部分をiとし
# その後スライスでお尻の部分判定をしようとした

# if k in s:
#   print('YES')
#   exit()

# x = 0
# for i in range(n):
#   if s[i] != k[i]:
#     x = i
#     break

# ここの条件がうまくできなかった…最後の1文字だけの時など。どうやったらうまくできるんだろう
# if k[x:] == s[n-1-x:n]:
#   print('YES')
# else:
#   print('NO')
