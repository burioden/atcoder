h,w = map(int,input().split())
g = [input() for _ in range(h)]

flg = 1

# 「#」黒の周り4方向（角であれば3または2方向）が全部「.」白だったら残念
# 全探索で周囲を見ていく

DX = [0,1,0,-1]
DY = [1,0,-1,0]

for i in range(h):
  for j in range(w):
    # 「#」黒をみつけたら
    if g[i][j] == "#":
      # 周りの4マスを調べるチェックループへ
      for k in range(4):
        nx = j + DX[k] # 周りのx軸
        ny = i + DY[k] # 周りのy軸
        # マスh*w内で、周りに#があったら大丈夫 チェックループを抜ける
        if 0 <= ny < h and 0 <= nx < w and g[ny][nx] == "#":
          break
      # チェックループを通過してしまったら全部「.」白のため残念
      else:
          flg = 0
          break

print('Yes' if flg else 'No')
