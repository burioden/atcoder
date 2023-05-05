import bisect

n,q = map(int,input().split())
a = sorted(list(map(int,input().split())))

# bisect_leftはソートされた配列aにxを挿入する場合、添字がどこに来るか？を返す
# 例えばケース1 a = {100 130 160} x = 120
# 添字1に挿入できる つまり x自信より上は2つあるので
# nからbisect.bisect_leftで返ってくる値を引くと答えになる
for i in range(q):
  x = int(input())
  print(n - bisect.bisect_left(a,x))
