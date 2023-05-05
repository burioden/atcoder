'''
端（1つのもの）が2つと、他のものは全て2つ
なぜWAが起こるかわからず、次数が2と1以外になるものがあったらNoを吐かせてみる
あ。頂点2の時は、パスグラフでも判定が違ったぞ。
ん？？？UnionFindしてみる？？？？
自身の根が全て0かつ、n-1 = mであったらYes
合体だ！！
'''

class UnionFind():
    def __init__(self, n):
        self.par = [-1] * n
        self.rank = [0] * n
        self.siz = [1] * n

    # x 自身の根
    def root(self, x):
        if self.par[x] == -1:
            return x
        else:
            self.par[x] = self.root(self.par[x])
            return self.par[x]

    # x と y は連結成分？
    def issame(self, x, y):
        return self.root(x) == self.root(y)

    # x を含むグループと y を含むグループをつなげる
    def unite(self, x, y):
        rx = self.root(x)
        ry = self.root(y)
        if rx == ry:
            return False
        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx
        self.par[ry] = rx
        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1
        self.siz[rx] += self.siz[ry]
        return True
    
    # x を含む根付き木のサイズを求める
    def size(self, x):
        return self.siz[self.root(x)]


n,m = map(int,input().split())
uf = UnionFind(n)

g = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int,input().split())
    uf.unite(a-1,b-1)
    g[a-1].append(b-1)
    g[b-1].append(a-1)
    

# 連結であるか判定 len(cnt) = 1であればOK
cnt = set()
for i in range(n):
  cnt.add(uf.root(i))

# 次数の判定
one = 0
two = 0

for i in g:
  if len(i) == 1:
    one += 1
  elif len(i) == 2:
    two += 1

# n = 2だけ例外
if n == 2:
  if one == 2:
    print('Yes')
    exit()

if one == 2:
  if n == two + 2:
    if len(cnt) == 1:
      print('Yes')
      exit()

print('No')
