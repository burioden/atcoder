n = int(input())
a = set(list(map(int,input().split())))

# aの中に1〜読める巻があればnから1を引きcanを+1、なければ2を引く（売る）
# 読めるものが何もなければ相殺され0になる
can = 0
while 0 < n:
  can += 1
  n -= 1 if can in a else 2

print(n+can)
