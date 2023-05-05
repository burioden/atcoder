'''

 ダメだった解答
 https://atcoder.jp/contests/abc283/submissions/37518253
 
 ↑の考え:孤立した要素があったら、i-1の全要素を反転すればよい？
 その分をカウントしよっと x 2回し
 
 この度は
 ・①i-1 ②i ③i+1 の要素が孤立しているかの判定をする
 ・操作の最小回数をdpでもつ
 
'''

# 入力
h,w = map(int,input().split())
g = [list(map(int, input().split())) for _ in range(h)]

# dp用
INF = float('inf')
dp = [[[INF for _ in range(2)] for _ in range(2)] for _ in range(h)]
dp[0][0][0] = 0
dp[0][0][1] = 1

for i in range(1,h):
  for j in range(2):
    for k in range(2):
      for l in range(2):
        
        # ①i-2 を判定する用の配列 t を作り 反転操作
        t = [-1 for _ in range(w)]
        for m in range(w):
          # 1行目のときはi-2が存在しないので
          if i != 1:
            t[m] = g[i-2][m]
          if j == 1:
            t[m] = 1 - t[m]
            
        # ②i-1 を判定する用の配列 o を作り 反転操作
        o = []
        for m in range(w):
          o.append(g[i-1][m])
          if k == 1:
            o[m] = 1 - o[m]

        # ③i  を判定する用の配列 c を作り 反転操作
        c = []
        for m in range(w):
          c.append(g[i][m])
          if l == 1:
            c[m] = 1 - c[m]
            
        # 孤立要素の判定（happy = 1 で 4方向どこかに仲間がいる）
        happy = 1
        
        for m in range(w):
          if (t[m] != o[m] and
              o[m] != c[m] and
              (m == 0 or o[m] != o[m-1]) and #コーナーケース
              (m == w-1 or o[m] != o[m+1])): #コーナーケース
            happy = 0 # :(
        
        # 最終行だけは、①t : i-2 の比較の必要がない
        if i == h-1:
          for m in range(w):
            if m == 0: # 最も左側
              if o[m] != c[m] and c[m] != c[m+1]:
                happy = 0
            elif m == w-1: # 最も右側
              if o[m] != c[m] and c[m] != c[m-1]:
                happy = 0
            else:
              if (o[m] != c[m] and c[m] != c[m-1] and
                  o[m] != c[m] and c[m] != c[m+1]):
                happy = 0
        
        # happyだったら、dp配列に最小の数を保存
        if happy:
          dp[i][k][l] = min(dp[i][k][l], dp[i-1][j][k]+l)
          

# dp配列を見ていき、最小の個数をansに入れていく
# 0だったらデカ数字（INF）のままなので、孤立を解消できない:(
ans = INF
for i in range(2):
  for j in range(2):
    ans = min(ans, dp[h-1][i][j])

print(ans if ans != INF else -1)
