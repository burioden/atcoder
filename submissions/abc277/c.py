from collections import defaultdict, deque
import sys
sys.setrecursionlimit(2*(10**5))

#DFSで解くのだ!!

n = int(input())
g = defaultdict(list)
for _ in range(n):
    a,b = map(int,input().split())
    g[a].append(b)
    g[b].append(a)

# 答え格納する辞書 重複を防げる
ans = {1}
# 今いる階と、前いた階を引数に持つデフ
def dfs(now,pre):
  # 今いる階をansに追加
  ans.add(now)
  # 今いる階のはしごたちを見る
  for to in g[now]:
    # これから行くところと、前いた階が違ったら
    if to != pre:
      # そして、今まで行ったことがなかったら
      if to not in ans:
        # 次へ進み、今いる階をansに追加
        dfs(to,now)
        ans.add(now)

# 1階からスタート（前いた階は存在しないものならなんでもOK）
dfs(1,-1)

# 行けた階で最大のものを出力
print(max(ans))
