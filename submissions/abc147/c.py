'''

・n人の証言を[[1人目が言ってること],[2人目が言ってること]]として保存しておく
  初期値は2次元配列だが、足していくと三次元配列になるよ（複数個証言が入る場合があるため）

・bit全探索をするよ
  まず各人の真偽の状態を2^nパターン作り出すよ

・状態の中に1があったら、1が立っている場所の人の証言を見ていくよ
  「確実に正しいこと」だけをチェックすればよいから、0は見なくていいよ
  
・各証言がいまのパターンに合致しているかを見て、違ったらフラグを折るよ

・全ての証言が合ってたら、そのパターンの1が立ってる人の総数が答えだよ
  とはいえ、全パターン見ていくから、max値を更新していくよ
  
'''

from itertools import product

n = int(input())
a = [[] for _ in range(n)]

for i in range(n):
  aa = int(input())
  for j in range(aa):
    x,y = map(int,input().split())
    x -= 1
    a[i].append([x,y])

ans = 0

for bit in product((0,1),repeat=n):
  flg = 1
  for i in range(n):
    if bit[i] == 1:
      for x,y in a[i]:
        if bit[x] != y:
          flg = 0
  if flg:
    ans = max(ans,bit.count(1))

print(ans)
