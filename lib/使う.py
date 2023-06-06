# 関数コーナー
# ----------------------------------

# 各桁けたの合計
def f(n):
    for i in range(1,n+1):
        x = sum(map(int, str(i)))
    return x

# nはmで 何回で割り切れる？
# -- 例：10は2で1回割れる（5は2で割り切れない）
def f(n, m):
    cnt = 0
    while n % m == 0:
        n //= m
        cnt += 1
    return cnt

# nが0になるまで、mで何回割り続けられるか
# -- 例：10を2で割り続けると4回で0になる
def f(n, m):
    cnt = 0
    while 0 < n:
      n //= m
      cnt += 1
    return cnt

# 素数判定
def f(n):
    if n < 2:
        return False
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

# n以下の素数はどれ？エラトステネスのふるい 素数の配列
# 0 or 1の配列で返す
def primes(n):
    sieve = [True] * ((n + 1) // 2)
    for i in range(1, (int(n ** 0.5) + 1) // 2):
        if sieve[i]:
            for j in range(i * 3 + 1, (n + 1) // 2, i * 2 + 1):
                sieve[j] = False
    res = [i * 2 + 1 for i, s in enumerate(sieve) if s]
    res[0] = 2
    return res

# 素因数分解[素因数,個数]

def f(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n ** 0.5 // 1)) + 1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])
    if temp != 1:
        arr.append([temp, 1])
    if arr == []:
        arr.append([n, 1])
    return arr

# 素因数分解 素因数だけ

def f(n):
    arr = set()
    temp = n
    for i in range(2, int(-(-n ** 0.5 // 1)) + 1):
        if temp % i == 0:
            while temp % i == 0:
                temp //= i
            arr.add(i)
    if temp != 1:
        arr.add(temp)
    if arr == set():
        arr.add(n)
    return arr

# 素因数分解 個数だけ

def f(n):
    cnt = 0
    temp = n
    for i in range(2, int(-(-n ** 0.5 // 1)) + 1):
        if temp % i == 0:
            while temp % i == 0:
                temp //= i
            cnt += 1
    if temp != 1:
        cnt += 1
    return cnt


# nの約数は何個ある？
def f(n):
    d = 0
    for i in range(1, n+1):
        if n % i == 0:
            d += 1
    return d

# nの約数は何？ 配列で返す
def f(N):
    res = []
    for i in range(1, N + 1):
        if i * i > N:
            break
        if N % i != 0:
            continue
        res.append(i)
        if N // i != i:
            res.append(N // i)
    res.sort()
    return res

# nとmの公約数は何？配列で返す

def f(n, m):
    d = []
    for i in range(1, max(n,m)+1):
        if n % i == 0 and m % i == 0:
            d.append(i)
    return d

# 回文判定
def f(s):
    n = len(s)
    flg = True
    for i in range(n):
        if s[i] != s[(n-1)-i]:
            flg = False
            break
    return flg


# nの階乗は？ 通常ver >> 10が限界
def f(n):
    v = 1
    for i in range(n, 1, -1):
        v *= i
    return v

# nの階乗は？ 再帰ver
from functools import lru_cache
@lru_cache
def f(n):
    if 0 < n:
      return n*f(n-1)
    return 1


# nは平方数？ 平方判定
def f(n):
    flg = False
    if n == 1 or n == 0:
      flg = True
    for i in range(1,n):
        if i*i == n:
            flg = True
            break
    return flg

# nまでの平方数はいくつある？ >> 0を除き、1はカウント
# 入力最大値が10の9乗である場合10,9に
import math
def f(n):
    cnt = 0
    for i in range(1, int(math.sqrt(pow(10, 9)))):
        if i*i <= n:
            cnt += 1
        else:
            break
    return cnt

# nまでの平方数は何？ 配列で返す
import math
def f(n):
    a = []
    for i in range(1, int(math.sqrt(pow(10, 9)))):
        if i*i <= n:
            a.append(i*i)
        else:
            break
    return a

# 辞書順で何番目？
from math import factorial
def f(L):
    x = 0
    while len(L) > 1:
        a = len([l for l in L if l < L[0]])
        x = x + a * factorial(len(L) - 1)
        L = L[1:]
    return x


# ----------------------------------
# 便利技コーナー
# ----------------------------------

# DXY配列 を グリッド マスの全探索に使う（8方向）
h, w = map(int, input().split())
g = [list(input()) for _ in range(h)] #文字列

DX = [0, 1, 0, -1, 1, 1, -1, -1]
DY = [1, 0, -1, 0, 1, -1, -1, 1]

# DX DY配列 グリッド マスの全探索に使う（4方向）
h, w = map(int, input().split())
g = [list(input()) for _ in range(h)] #文字列

DX = [0, 1, 0, -1]
DY = [1, 0, -1, 0]

## 何かを見つけたら入る時 文字列
for i in range(h):
  for j in range(w):
    # 「#」黒をみつけたら
    if g[i][j] == "#":
      # 周りの4マスを調べるチェックループへ
      for k in range(4): #8方向なら8に
        nx = j + DX[k] # 周りのx軸
        ny = i + DY[k] # 周りのy軸
        # マスh*w内で、周りに#があったら大丈夫 チェックループを抜ける
        if 0 <= ny < h and 0 <= nx < w and g[ny][nx] == "#":
          break
      # チェックループを通過してしまったら全部「.」白のため残念
      else:
          flg = 0
          break
      
## ただ探すとき？？ 文字列 ※
for i in range(h):
  for j in range(w):
    # 「#」黒をみつけたら
    if g[i][j] == "#":
      # 周りの4マスを調べるチェックループへ
      for k in range(4): #8方向なら8に
        nx = j + DX[k] # 周りのx軸
        ny = i + DY[k] # 周りのy軸
        # マスh*w内で、周りに#があったら大丈夫 チェックループを抜ける
        if 0 <= ny < h and 0 <= nx < w and g[ny][nx] == "#":
          break
      # チェックループを通過してしまったら全部「.」白のため残念
      else:
          flg = 0
          break



# 累積和 >> 配列の中身を全て足したものに書き換える
n = int(input())
a = list(map(int, input().split()))

for i in range(1, n):
    a[i] += a[i - 1]


# 累積和 >> 配列の中身を全て足したものを新しいリストに追加
n = int(input())
li = list(map(int, input().split()))
sum_li = li[:]

for i in range(1, n):
    sum_li[i] += sum_li[i - 1]

print(sum_li)


# 要素の出現回数を数える
# liの中で一番多く出現している要素は？
import collections

li = []
li_c = collections.Counter(li)
x = li_c.most_common()[0][0]

# liの中で一番多く出現している要素の出現回数は？
import collections

li = []
li_c = collections.Counter(li)
x = li_c.most_common()[0][1]

# 出現回数をプリント
for i,d in li_c.items():
    print(d)

# 出現要素をプリント
for i,d in li_c.items():
    print(i)


# 二分探索
# 初期値のng,okを受け取り,is_okを満たす最小(最大)のokを返す
# まずis_okを定義すべし
# ng ok は  とり得る最小の値-1 とり得る最大の値+1
# 最大最小が逆の場合はよしなにひっくり返す

def is_ok(arg):
    # 条件を満たすかどうか？問題ごとに定義
    pass

def bisect(ng, ok):
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok

# 二分探索 答えが出るまで、midを取り続ける

def f(X):
  return X * (X * (X + 1) + 2) + 3

n = float(input())

left = 0
right = 100000

while (right - left > 10 ** -4):
  mid = (left + right) / 2
  if (f(mid) < n):
    left = mid
  else:
    right = mid
    
print(left)


# nに対する正確な四捨五入x
n = float(input())
x = int((n * 2 + 1) // 2)


# 一文字目だけ大文字に、あとは全て小文字に
# capitalize
s = input()
print(s.capitalize())

# もし大文字の時はの判定は.isupper(小文字は.islower)


# フィボナッチ数列（1, 1, 2, 3, 5, 8）

def f(n):
  a, b = 0, 1
  li = []
  while n:
    n -= 1
    li.append(b)
    a, b = b, a + b
  return li


# ----------------------------------
# グラフ・木コーナー
# ----------------------------------

# 隣接リスト 木 グラフ 辺の重みがない
# nは辺の数、mは頂点の数
n,m = map(int,input().split())
g = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int,input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)  # 有向グラフなら消す
print(g)

# 隣接リスト 木 グラフ 辺の重みがある(コスト)
# vはコスト
n,m = map(int,input().split())
g = [[] for _ in range(n)]
for _ in range(n):
    u,v,w = map(int,input().split())
    g[u-1].append([v-1,w])
    g[v-1].append([u-1,w])  # 有向グラフなら消す
print(g)


# 隣接行列 辺の重みがない
n,m = map(int,input().split())
g = [[0]*n for _ in range(n)]
for _ in range(m):
    a,b = map(int,input().split())
    g[a-1][b-1] = 1
    g[b-1][a-1] = 1  # 有向グラフなら消す
print(g)

# 隣接行列 辺の重みがある コストがそのまま数字になって格納される
n,m = map(int,input().split())
g = [[0]*n for _ in range(n)]
for _ in range(m):
    u,v,w = map(int, input().split())
    g[u-1][v-1] = w
    g[v-1][u-1] = w  # 有向グラフなら消す
print(g)


# 座標圧縮----------------------------------
# 圧縮したい配列
a = [7,124,915,133,6333,2165]

# 重複さよならしてソート
b = sorted(set(a))

# bの各要素は、下から何番目？
z = {v:i+1 for i,v in enumerate(b)}

# 圧縮したa配列
print(list(map(lambda v: z[v], a)))

# ----------------------------------
# DFS

from collections import defaultdict, deque
import sys
sys.setrecursionlimit(2 * (10 ** 5))

n = int(input())
g = defaultdict(list)
for _ in range(n):
    a,b = map(int,input().split())
    g[a].append(b)
    g[b].append(a)

# 答え格納する辞書 
ans = {1}

# 今いる階と、前いた階を引数に
def dfs(now,pre):
      # 今いる頂点をansに追加
  ans.add(now)

    # 今いるところの辺全てを見る
  for to in g[now]:
        # これから行くところと、前いたところが違ったら
    if to != pre:
              # そして、今まで行ったことがなかったら
      if to not in ans:
               # 次へ進み、今いるところをansに追加
        dfs(to,now)
        ans.add(now)

# 開始と、適当な存在しない前いたところ
dfs(1,-1)

print(max(ans))

# 2点間距離（ユークリッド）二重for文 二次配列
x = ((a[i][0] - a[j][0])**2 + (a[i][1]- a[j][1])**2)**0.5

# 2点間距離（ユークリッド距離）を求める関数 
def df(A,B,C,D):
  return (((A-C) ** 2) + ((B-D) ** 2))**0.5

# ----------------------------------
# BFS

from collections import defaultdict, deque

n = int(input())
g = defaultdict(list)
for _ in range(n):
    a,b = map(int,input().split())
    g[a].append(b)
    g[b].append(a)

# 情報を一次保存する筒
que = deque()
que.append(1)

# 答えを格納する辞書
ans = {1}

# 筒の中身がなくなるまで
while que:
  # vは探索対象の階 筒のいちばん左を消し、消した値をvに代入
  v = que.popleft()
  # g[v]、つまり探索対象の階にある全部のはしごを見ていく
  for i in g[v]:
    # もし未探索の階なら
    if not i in ans:
      # 調べる対象の階を筒にストック
      que.append(i)
      # 探索済みの階にもストック 辞書だと重複が合体される
      ans.add(i)

# 辿り着けた最大の階数を出力
print(max(ans))


# ソート itemgetter

from operator import itemgetter
# a.sort(key=itemgetter(1))


# 長い入力の時
import sys

array = []
for line in sys.stdin.readlines():
    array.append(line.rstrip())
print(array)


# 辞書順の順列・組み合わせの列挙をする時はitertoolsを使う
# 文字列Sを昇順に並べたk番目を出力せよの問題
import itertools

s,k = input().split()
k = int(k)

S = itertools.permutations(s, len(s))
S = sorted(set(S))

print(*list(S[k-1]),sep="")

import itertools

n = int(input())

# 重複アリで順列を作る時はproduct
s = list(itertools.product('abc',repeat=n))
s.sort()
for i in s:
  print(*i,sep="")

# lambda

#全てに1を足す
a = list(map(lambda x: int(x)+1,input().split()))
# 全てをマイナス数値にする
a = list(map(lambda x: int(x)*-1,input().split()))
#文字列を数値に変換(chrで元に戻るよ)
a = list(map(lambda x: ord(x) - ord("a"),input().split()))

# ライブラリコーナー
# https://amateur-engineer-blog.com/python-bisect/
import bisect
bisect.insort(a, x) # a配列に、xを入れる
x = bisect.bisect_right(a,13) #aの中に13を入れたら？の最大インデックスが返ってくる
x = bisect.bisect_left(a,13) #aの中に13を入れたら？の最小インデックスが返ってくる

import heapq
# 配列aをヒープ化
heapq.heapify(a)
# 最大 を取りたい場合は先に-aiしておく
# 入れる時も取り出す時も-にする
x = -heapq.heappop(a)
heapq.heappush(a,-x)

# 最小でよければこちら
x = heapq.heappop(a)
heapq.heappush(a,x)



# dp のきほん----------------------------------

n = int(input())
h = list(map(int, input().split()))

# 初期化
# 最小化のため最大値で初期化
dp = [10**5+1] * n

# 初期条件
# 柱0の移動コストは0
# 柱1への最小コストは柱0からの場合のみ
dp[0] = 0
dp[1] = abs(h[1] - h[0])

# 解を求めるまで繰り返す
for i in range(2, n):
    # dpテーブルの解を利用して解を求める
    # 柱iまでの最小コストは柱i-1からの移動か柱i-2からの移動の小さい方
    dp[i] = min(abs(h[i] - h[i - 1]) + dp[i - 1], abs(h[i] - h[i - 2]) + dp[i - 2])

print(dp[-1])


# いもす法----------------------------------

# いもす区間
n = 7
# いもす配列
d = [0] * n
# l = 開始 r = 終了 v = 加算したい
s = [[1,3,2],[3,3,3],[0,5,1]]

for l, r, v in s:
  d[l] += v
  if r + 1 != n:
    d[r + 1] += -v

# 累積和用配列
r = [0] * n
r[0] = d[0]

# 累積する① 新しい配列を作り
for i in range(1, n):
  r[i] = r[i-1] + d[i]

# 累積する② ゼロうめしてからdに直接
d.insert(0, 0)
for i in range(n):
  d[i+1] += d[i]

print(d) #ゼロうめされてるから1つ長い
print(r)


# UnionFind----------------------------------

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

n = int(input())
n,m = map(int,input().split())
# よしなに入力
uf = UnionFind(n)


# ----------------------------------


# 積の総和 mod
n = int(input())
a = list(map(int,input().split()))

MOD = 1000000007
s = sum(a)
t = sum(map(lambda x : x * x ,a))

print((s*s-t)//2 % MOD)


# 曜日
d = {'Monday': 5, 'Tuesday': 4, 'Wednesday':3 , 'Thursday': 2, 'Friday': 1, 'Sunday': 0, 'Saturday': 0}


# 等差数列の和 1〜nまで
((n + 1) * n) // 2


# 複数の最小公倍数
import math
import functools

def my_lcm_base(x, y):
    return (x * y) // math.gcd(x, y)

def lcm(*integers):
    return functools.reduce(my_lcm_base, integers)

# 複数の最大公約数

import functools

def gcd(*integers):
    return functools.reduce(math.gcd, integers)



# x/yの四捨五入
x = 2
y = 1

(x + y // 2) // y

# 床関数（切り捨て）
x // y

# 天井関数（切り下げ） 
(x + y - 1) // y

# 回転行列 二次元配列aを90度回転
rotate = lambda a: [list(x)[::-1] for x in zip(*a)] 

# 転置 列と行を逆に zip
transpose = lambda a: [list(x) for x in zip(*a)]