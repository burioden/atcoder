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
a = [list(map(int, input().split())) for _ in range(m)]

cnt = 0
for x,y in a:
    uf.unite(x-1,y-1)

for i in range(n):
    if uf.root(i) == i:
        cnt += 1
        
print(cnt)
