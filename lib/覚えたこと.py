# ----------------------------------

# ITP1_3_d (https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_3_D&lang=ja)

import collections
import math
from cmath import sqrt


a, b, c = map(int, input().split())

# リストは数値の空でも書けるよ
list = []

# rangeは最後の値に注意。未満だから、bも含めたい場合は+1
for i in range(a, b + 1):
    # list.append(i)、積極的に使おう！
    list.append(i)

count = 0
# rangeは最後の値を「含めない」という性質を使って、out of rangeを防ぐ。
for i in range(0, len(list)):
    if c % list[i] == 0:
        count += 1

print(count)

# ----------------------------------

# 小数点は、format関数で桁数を指定できる
"{:.5f}".format(a/b)

# ----------------------------------

# 1列に整数と文字列が混じってるときは、最初に文字列で入れて、あとからintに変換

a, op, b = input().split()

a = int(a)
b = int(b)

# 入力は、1列であれば簡単に受け取れるよ
a = list(map(int, input().split()))

# ,end=""で、終わりにだけ入れるものを設定できる
# sep=""で、終わったら改行でセパレートしてね（改行してね）とできる
print(a*b, end="\n")
print(a*b, sep="")

# forでend=""とすると、次の処理のprintと繋げることができる！！

while True:
    h, w = map(int, input().split())
    if h == 0 and w == 0:
        break
    for i in range(h):
        for j in range(w):
            if (i+j) % 2 == 0:
                print("#", end="")
            elif (i+j) % 2 == 1:
                print(".", end="")
        print()
    print()


# 目的の数字が入ってるか確認するときは、文字列str(i)に直して in str(i)で入ってるかどうかを判断（例えば、1桁目だけに3がある場合など）

n = int(input())
print(end=" ")
for i in range(1, n + 1):
    if i % 3 == 0:
        print(i, end=" ")
    elif "3" in str(i):
        print(i, end=" ")


# ----------------------------------

# if if ifと続けると、2番目のifが1番目のifも条件に含めてしまうため、重複で条件が重なってしまう。
# が、逆に言えば elif は、前の条件と重複しているものは書かなくて良い！
# つまり、A==Bのみの時は、絶対的なので、if if ifで書いてOK！
# そして、各要素に番号をつけてあるなしの判断するだけなら、2次配列にしないでもできる！！

n = int(input())
card = list()

for i in range(n):
    x, y = input().split()
    y = int(y)
    if x == "S":
        card.append(y)
    if x == "H":
        card.append(y+13)
    if x == "C":
        card.append(y+26)
    if x == "D":
        card.append(y+39)

for j in range(1, 53):
    if not j in card:
        if j <= 13:
            print("S " + str(j))
        elif j <= 26:
            print("H " + str(j-13))
        elif j <= 39:
            print("C " + str(j-26))
        else:
            print("D " + str(j-39))


# ----------------------------------

# 3つのものに対しての正誤判定は、3つ存在する！

w1 = list(input())
w2 = list(input())

if w1[0] == w2[2] and w1[1] == w2[1]:
    print("YES")
else:
    print("NO")


# ----------------------------------

# ↑と、覚えたのに・・・場合分けその1
# 構成する要素の数の取得は len で、setでまとめちゃえ！

a, b, c = map(int, input().split())
print(len(set([a, b, c])))


# ----------------------------------

# 文字列は不変なので[i]で入れ替えられない。
# ので、replaceメソッドで入れ替えましょう

s = input()

print(s.replace(',', ' '))

# 複数入力！二次配列
n = int(input())

a = []
for _ in range(n):
    a_inner = list(map(int, input().split()))
    a.append(a_inner)

# 複数入力！ただの配列
n = int(input())
a = [input() for _ in range(n)]


# 重複期間の値の数を見つける
a, b, c, d = map(int, input().split())

l1 = []
l2 = []

for i in range(a, b):
    l1.append(i)
for i in range(c, d):
    l2.append(i)

l1_l2_and = set(l1) & set(l2)

l1_l2_and_list = list(l1_l2_and)

print(l1_l2_and_list)


# pythonはli[-1]で最後から数えられちゃうから、インデックスをマイナス指定したいときはrange(1,n)に！

n = int(input())
list = list(map(int, input().split()))

count = 0

for i in range(1, n):
    if list[i] > list[i-1]:
        count += 1

print(count)

# インデックス番号は連番なので、1~9番目、って使い方もできるんだよ。

n = int(input())
li = list(map(int, input().split()))

cnt = [0]*9

for i in li:
    cnt[i-1] += 1

for i in cnt:
    print(i)


# 素数判定
# 素数とは、2以上且つn自身でしか割り切れないもの

n = int(input())

# 素数判定のflg(prime=素数)を作る
prime = 1

# 1だったら素数じゃないよ！
if n == 1:
    prime = 0
# 2以上n以下で割り切れたら素数じゃないよ！
else:
    for i in range(2, n):
        if n % i == 0:
            prime = 0

if prime:
    print("Yes")
else:
    print("No")



# 約数(div)判定

n = int(input())

# 1からnまで調べる　n自身も含めたいので+1
for i in range(1, n+1):
    # 約数判定divさん
    div = 0
    # 1からiまで（iを含めたいので+1）
    for j in range(1, i+1):
        # iが1~i(j)で割り切れる数があったら、それは約数だよ
        if i % j == 0:
            div = 1

# 約数は何かを出力する

n = int(input())

for i in range(1, n+1):
    if n % i == 0:
        print(i)


# ----------------------------------
# 回文判定

s = input()
# sの長さをとる
n = len(s)
# 初期値はTrue
flg = 1
# 0~n-1(文字の長さ、インデックスのためマイナス)の間
for i in range(n):
    # sの頭からi番目と、後ろからi番目（インデックスのためマイナス）を比較して違ったらFalseに
    if s[i] != s[(n-1)-i]:
        flg = 0
if flg:
    print("Yes")
else:
    print("No")




# ----------------------------------
# アルファベットを文字コードに変換、文字コードからアルファベットに変換

n = ord('a')
s = chr(n)

# upper-case A-Z 65 <= n <= 90
print([chr(i) for i in range(65,65+26)])
print([chr(ord("A")+i) for i in range(26)])
# lower-case a-z 97 <= n  <= 123
print([chr(i) for i in range(97,97+26)])
print([chr(ord("a")+i) for i in range(26)])

# lower -> upper
+32

# 条件に「13以上」「6以上12以下」を入れるときは、大きい数から順番に

if a > 12:
    print(b)
elif a > 5:
    print(b//2)


# ----------------------------------

# 階乗
# for文は逆からもできる

def fac(n):
    v = 1
    for i in range(n, 1, -1):
        v *= i
    return v

# ----------------------------------

# 同じiに対して処理を複数回したい場合は、for文の中にwhileを入れると叶う
# if〜だとiを1回しか使えない

for i in range(10, 0, -1):
    while n >= fac(i):
        n -= fac(i)


# dic型はオブジェクト

s = input()
week = {"Monday": 5, "Tuesday": 4, "Wednesday": 3, "Thursday": 2, "Friday": 1}

if s in week:
    ans = week[s]

print(ans)


# 受け取るべきところに何もないとインプットができずエラーを吐く（そりゃそうだ）

# (の中では改行してもいいんだよ！)

# まさか"/"を含む文字列を比較できるとは

print(
    "H"
    if input() <= "2019/04/30"
    else "TBD"
)

# 文字列を逆順にしたいときは「s[::-1]」
# インデックス番号は、最初のものは.indexで取得可能

s = input()
rs = s[::-1]

start = s.index("A")+1
end = len(s)-rs.index("Z")+1

print(end-start)

# nの平方数はいくつあるか調べる
# ifでいきなり出力するよりも、値を更新した方が良い
# 平方根はimport mathする


n = int(input())

ans = 0

# 入力最大値が10の9乗である場合
for i in range(1, int(math.sqrt(pow(10, 9)))):
    if i*i <= n:
        ans += 1
    else:
        break

print(ans)

# nが平方数であるか調べる

n = int(input())

flag = 0

for i in range(1, n):
    if i*i == n:
        flag = 1

print("Yes" if flag else "No")

# 組み合わせ1-1,1-2,1-3,1-4,2-3,2-4,3-4を調べる2重ループ

a = [int(input()) for i in range(6)]

flag = 1

for i in range(5):
    for j in range(i+1, 5):
        if a[j] - a[i] > a[5]:
            flag = 0
            break

print("Yay!" if flag else ":(")


# 累積和 [1,2,3] >> [1,1+2,1+2+3] >> [1,3,6]

n = int(input())
li = list(map(int, input().split()))

for i in range(1, n):
    li[i] += li[i-1]

# 累積和 >> 配列の中身を全て足したものを新しいリストに追加
# listは参照元を同じとしてしまうので、新たに複製する時にli[:]としてあげる
n = int(input())
li = list(map(int, input().split()))
sum_li = li[:]

for i in range(1, n):
    sum_li[i] += sum_li[i-1]

print(sum_li)

# ansにでか数字入れておく

ans = 100000

# 差分を求める
# t = 1の時 >> s1 = ["1",3,6] >> 1
# t = 1の時 >> s2 = [1,3,"6"] - s1("3") = 6 - 1 >> 5
# t = 1の時の差は5
# t = 2の時 >> s1 = [1,3,"6"] >> 6
# t = 2の時 >> s2 = [1,3,"6"] - s1("6") = 6 - 6 >> 0
# t = 2の時の差は0
# aよりbの方が小さかったら、aをbに置き換える
# そうじゃなかったら、そのまま

for t in range(n):
    s1 = li[t]
    s2 = li[n-1] - s1
    if abs(s1 - s2) < ans:
        ans = abs(s1 - s2)

print(ans)

# aからb,cからdの距離の重なっているところを調べるとき 重複距離
# bとdで小さい方から、aとcの大きい方を引いて、0より大きいものを出力

a, b, c, d = map(int, input().split())

upper = min(b, d)
lower = max(a, c)

print(max(0, upper-lower))

# 配列を改行区切りで出す

print(*ans, sep='\n')

# 1〜nまでの各けたの合計を求める
# リスト内包表記で合計を出してしまう

n = int(input())

for i in range(1, n+1):
    num = sum([int(k) for k in str(i)])
    print(num)


# 各けた計算その2
# mapでstr型にしたそれぞれのケタをintにし、足す。やばい
# a < 欲しい値 < bもできるお

n, a, b = map(int, input().split())
ans = 0

for i in range(1, n+1):
    if a <= sum(map(int, str(i))) <= b:
        ans += i

print(ans)


# popは削除とコピーを同時にしてくれる（戻り値として消した値を返してくれる）
# if list(この場合はa):と書くと、listに何か存在している時だけの条件分岐ができる

a = list(input())
b = list(input())
c = list(input())

now = "a"

while 1:
    if now == "a":
        if a:
            now = a.pop(0)
        else:
            print("A")
            break
    elif now == "b":
        if b:
            now = b.pop(0)
        else:
            print("B")
            break
    else:
        if c:
            now = c.pop(0)
        else:
            print("C")
            break

# 排他的論理和XORは、差分を取るのに使う

s = sorted(input())
ss = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

ans = set(s) ^ set(ss)

print(" ".join(map(str, ans)))


# 出現回数を数える
# 少ない値を吐き出す、回数の場合は[-1][1]

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

li_x = collections.Counter([x1, x2, x3])
li_y = collections.Counter([y1, y2, y3])

print(li_x.most_common()[-1][0], li_y.most_common()[-1][0])


# zip(*[map〜])で縦と横を入れ替えてる　列を行に、行を列に
# 3つ以上の排他的論理和は、真が偶か奇かを判断している

x, y = zip(*[map(int, input().split()) for _ in range(3)])

X = x[0] ^ x[1] ^ x[2]
Y = y[0] ^ y[1] ^ y[2]

print(X, Y)


# ----------------------------------
# abc047_b

w,h,n = map(int, input().split())
# w個（w列）の0をh行作る
s_li = [[0]*w for _ in range(h)]

# 取り入れながら処理する
for i in range(n):
    x,y,q = map(int, input().split())
    for j in range(w):
        for k in range(h):
            if q == 1 and j < x:
                s_li[k][j] = 1
            elif q == 2 and j >= x:
                s_li[k][j] = 1
            elif q == 3 and k < y:
                s_li[k][j] = 1
            elif q == 4 and k >= y:
                s_li[k][j] = 1

# 2次配列を合計してさらに合計することにより、0の数を数えている
# 2次配列の中身をカウント
ans = sum([sum(i == 0 for i in a)for a in s_li])

print(ans)


# ----------------------------------
# 二分探索　テンプレ関数
# https://atcoder.jp/contests/abc146/tasks/abc146_c

a,b,x = map(int, input().split())

# この関数の中身を書き換える
def is_ok(mid):
  if (a * mid) + (b * len(str(mid))) <= x:
    return True
  else:
    return False

# 二分探索（左がOK 最大 ver）
def bs(ok, ng):
  while ng - ok > 1:
    mid = (ok + ng)//2
    if is_ok(mid):
      ok = mid
    else:
      ng = mid
  return ok

ans = bs(0, 10**9+1)
print(ans)

# シンプルなwhile

a,b,x = map(int, input().split())

ok = 0
ng = 10**9+1

while ng-ok > 1:
  n = (ok + ng)//2
  d = len(str(n))
  if a*n + b*d <= x:
    ok = n
  else:
    ng = n

print(ok)

# 左側がNG 最小を出したい場合

def is_ok(mid):
    # if 条件:
        return True
    # else:
        return False

def ds(ng,ok):
    while ok-ng > 1:
        mid = (ok - ng)//2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid


# sorted(a)されたものは元のリストに影響を与えないから、
# sorted(a).indexで元のリストの降順インデックスが取れる

a = [int(input())for i in[0]*3]

for x in a:
  print(3-sorted(a).index(x))


# round関数は0.5を1にしてくれない。時もある。なんかよくわからんが
# 正確に出したい時は、2倍して1を足し、2で割り切る

n = float(input())

print(int((n * 2 + 1) // 2))


# 最小と最大を先に作り、その中に目的の数字はあるか

a,b = map(int,input().split())
 
min = 1*a
max = 6*a
 
if min <= b <= max:
  print('Yes')
else:
  print('No')

# ----------------------------------
# 数値をリストにして入力

s = list(map(int,list(input())))

# 列ごとに格納しなおした配列 1行目は1列目
# orは「どちらかが1ならば1」を格納
# or演算は、数値じゃないとできない！！
c = [
  s[6],
  s[3],
  s[1] or s[7],
  s[0] or s[4],
  s[2] or s[8],
  s[5],
  s[9]
]

# 文字列にする
col = ''.join(map(str, c))

# スプリットであるパターン（101,1001,10001,100001,1000001 を作る）
split_p = ["1"+"0"*i+"1" for i in range(1,6)]

# 1が倒れていたらスプリットの可能性がある
# スプリットであるパターンと比較
# スプリットを見つけたらYesを吐き終了
if s[0] == 0:
  for s in split_p:
    if s in col:
      print('Yes')
      exit()

print('No')


# k進数の桁数は、nをkで割り続けた数で表すことができる

n,k = map(int,input().split())

cnt = 0

while n > 0 :
  n = n//k
  cnt += 1

print(cnt)

# n進数を10進数にする時は、扱いたい数値を文字列にする必要あり

k = int(input())
a,b = input().split()

a,b = int(a,k),int(b,k)

print(a*b)

# ----------------------------------

# 剰余計算で9と0が隣り合ってる時に判定できるよ

x = list(map(int,input()))
a = x[0]
b = x[1]
c = x[2]
d = x[3]

ans = "Strong"

if len(set(x))==1:
  ans = "Weak"
elif ((a+1)%10==b%10) and ((b+1)%10==c%10) and ((c+1)%10==d%10):
  ans = "Weak"

print(ans)

# 一文字目だけ大文字に、あとは全て小文字に
# capitalize

s = input()

print(s.capitalize())

# ゼロうめはzfill
n = int(input())

h = str(n//60//60%60).zfill(2)
m = str(n//60%60).zfill(2)
s = str(n%60).zfill(2)

print(h+":"+m+":"+s)

# bit全探索その1

n,x = map(int,input().split())
a = list(map(int,input().split()))

ans = 0

for i in range(n):
  # xをi回右シフト（2進数に変換）し、2進数にしたx[i]に1のフラグが立ってるか
  if (x>>i) & 1:
    ans += a[i]

print(ans)

# bitについて
# << 左シフト 2のn乗
# 2^2 = 4
print(1 << 2)
# 2^3 = 8
print(1 << 3)

n = int(input())
a = list(map(int,input().split()))

# リスト内包表記はsumなど関数内でも使える
ans = sum(1 << x for x in a)

print(ans)

# 整数nの2進数表記で、x番目のフラグは1かどうか
n,x = map(int,input().split())

# x番目に1を押し込む、みたいなので覚えるといいかも
if n & (1 << x):
    print("Yes")
else:
    print("No")

# 再帰の時に使おう
# 同じ引数が与えられた時に再計算結果を返すことにより、計算量を削減

from functools import lru_cache

n = int(input())

@lru_cache
def f(k):
  if k == 0:
    return 1
  else:
    k = f(int(k/2))+f(int(k/3))
    return k

print(f(n))

# ----------------------------------
# 条件の中にあるかないかで引く数を設定できる

n = int(input())
a = set(list(map(int,input().split())))

# aの中に1〜読める巻があればnから1を引きcanを+1、なければ2を引く（売る）
# 読めるものが何もなければ相殺され0になる
can = 0
while 0 < n:
  can += 1
  n -= 1 if can in a else 2

print(n+can)


# ----------------------------------
# 11月の宿題！座標！！
# https://atcoder.jp/contests/abc258/tasks/abc258_b #自力で解けるように座標頑張る
# https://atcoder.jp/contests/abc007/submissions/32179357 #理解する、わからんとこ聞く
# https://kenkoooo.com/atcoder/#/training/Boot%20camp%20for%20Beginners/1 69問余裕だな

n = int(input())
a = [[*input()] for _ in range(n)]
ans = 0

for i in range(n):
  for j in range(n):
    for x,y in [(1,0),(0,1),(1,1),(1,-1)]:
      s = ""
      for k in range(n):
        s += a[(i+k*x)%n][(j+k*y)%n]
      ans = max(ans,int(s),int(s[::-1]))

print(ans)


# ----------------------------------
# input時にlambdaで加工

n,m = map(int,input().split())
a = list(map(lambda x: (int(x), 0), input().split()))
b = list(map(lambda x: (int(x), 1), input().split()))
c = sorted(a + b)

print(a)
print(b)
print(c)


# 辞書でデータを管理

n = int(input())
m = int(input())
a = []
for i in range(m):
  x,y,c = map(int, input().split())
  a.append([x,c])

dic = {}
# aに入ってる二次配列をdicへ格納
for r in a:
  # a[x,c]をそれぞれtime,countという変数に
  time,count = r
  # time（例えば3）がなかったら、countを0にして新規作成
  if time not in dic:
    dic[time] = 0
    # 同じtimeのものはcountを足し続ける
  dic[time] += count

# print(dic) してみて！
# 最後にdicのcount部分（value）を回数に処理すれば完成

ans = 0
for v in dic.values():
  ans += v//n if v%n == 0 else (v//n)+1

print(ans)

# 2つセットな二次配列からの参照は for i in li　と i[0] & i[1]ペアでできる

n,k = map(int,input().split())
li = sorted([list(map(int, input().split())) for _ in range(n)])

for i in li:
  if i[0] <= k:
    k += i[1]

print(k)


# マスの全探索

DXY = [(0,1),(1,0),(0,-1),(-1,0),(1,1),(1,-1),(-1,-1),(-1,1)]

h,w = map(int,input().split())
s = [list(input()) for _ in range(h)]

s = [[0 if i == "." else "#" for i in r] for r in s]

for i in range(h):
  for j in range(w):
    if s[i][j] == "#":
      continue
    for k in DXY:
      # 難関だった…iは高さ、jは幅、と考えりゃそりゃそうだった
      ni,nj = k[1] + i, k[0] + j

      if ni < 0 or ni >= h or nj < 0 or nj >= w:
        continue

      if s[ni][nj] == "#":
        s[i][j] += 1

for r in s:
  print(*r,sep="")



# スライスについて
s = "ABCDE"
s[0] = "A"
s[0:1] = "A"
s[0:2] = "AB"
s[-2] = "D"
s[:-2] = "ABC"

# インデックス番号である、〜まで、は未満になる
# -2を含めず、って覚えるといいかも

# 文字の一部を書き換えることはできないけれど
# 文字全体を書き換えることはできる

# https://atcoder.jp/contests/abc212/tasks/abc212_c
n,m = map(int,input().split())
a = sorted(list(map(int,input().split())))
b = sorted(list(map(int,input().split())))

# ソートして、比べていく
# 2つの配列をそれぞれ比べて、小さい方の配列のコマを次に進める
# そうすると、おのずと大きい方の値に近いものが見つかる
# もし越えても、常にminで記録しているので大丈夫

i,j = 0,0
ans = 10**9

while i<n and j<m:
  ans = min(ans,abs(a[i]-b[j]))
  if a[i] < b[j]:
    i += 1
  else:
    j += 1

print(ans)


# 逆からforを回したいときはreversed(range(n))！
for i in reversed(range(n)):
    pass


# 文字列の最後の1文字を取って、最初の一文字に足す

s = list(input())
li = [[] for i in range(len(s))]

for i in range(len(s)):
  x = s.pop()
  li[i] = [x]+s
  s = [x]+s

print(*min(li),sep="")
print(*max(li),sep="")


# 座標圧縮

import bisect

n = int(input())
a = list(map(int,input().split()))

b = [0]*n
aa = sorted(set(a))

for i in range(n):
  b[i] = bisect.bisect_left(aa,a[i]+1)

print(*b)


# 出現回数が一番多いものを全て排出

import collections

n = int(input())
li = [input() for i in range(n)]

li_c = collections.Counter(li)
# マックス回数
m = li_c.most_common()[0][1]
# もし出現回数v([0][1])がマックス回数と同じならば、i([0][0])を格納
k = [i for i,v in li_c.items() if v == m]
k.sort()

for i in range(len(k)):
  print(k[i])


# 入力しながら、何番目の要素だったかを記録する
# 50を-50にしておけば、ソートを逆順にできる
# インデックス番号+1にしているものをプリントすればよし

n = int(input())
s = []
for i in range(n):
  a,b = input().split()
  b = int(b)
  s.append([a,-b,i+1])

s = sorted(s)

for i,d,k in s:
  print(k)


# 二次元配列の重複要素は、tupleにすることでsetにでき排除できる

n = int(input())
a = []
for i in range(n):
  A,*B = map(int,input().split())
  B = tuple(B)
  a.append(B)

print(len(set(a)))


# 二次元配列の中でd重ループを回すときにはリスト内包表記

n,d = map(int,input().split())
x = [list(map(int, input().split())) for _ in range(n)]

ans = 0

def f(n):
    flg = False
    if n == 1 or n == 0:
      flg = True
    for i in range(1,n):
        if i*i == n:
            flg = True
            break
    return flg

for i in range(n):
  for j in range(i):
    if f(sum([(x[i][l]-x[j][l])**2 for l in range(d)])):
      ans += 1

print(ans)



# i==jの時以外はそれぞれの比較をしたときに大きいもののなかで
# 小さいものを出す

n = int(input())
a = []
b = []
for i in range(n):
  A,B = map(int,input().split())
  a.append(A)
  b.append(B)

ans = 10**6

for i in range(n):
  for j in range(n):
    ans = min(ans,a[i]+b[j] if i==j else max(a[i],b[j]))

print(ans)


# 二次元配列を2項めを基準にソート

n,m = map(int,input().split())
li = [list(map(int, input().split())) for _ in range(n)]

s = sorted(li,key=lambda x: x[1])


# 2点間の距離比較（a=[2,3]など、特定の比較対象が与えられている場合）
# 2点 (a,b),(c,d) 間の距離は  ((a-c)**2 + (b-d)**2)**0.5
# **0.5は、答え出力の時に取り扱うとよい


n,k = map(int,input().split())
a = list(map(int,input().split()))
s = [list(map(int, input().split())) for _ in range(n)]

ans = 0
for i in range(n):
  # 10の18乗
  m = 1e18
  for l in a:
    m = min(m,(s[i][0] - s[l-1][0])**2 + (s[i][1] - s[l-1][1])**2)
  ans = max(ans,m)

print(ans**0.5)

# 組み合わせを楽に探せる

from itertools import combinations
n = int(input())

l = list(map(int,input().split()))

ans = 0

for a, b, c in combinations(l,3):
  if a != b and b != c and c != a:
    if abs(b-c) < a < b + c:
      ans += 1

print(ans)


# 2回zipすると、列と行両方での操作が行える

h,w = map(int,input().split())
a = [list(input()) for _ in range(h)]

a = [i for i in a if "#" in set(i)]
a = list(zip(*a))
a = [i for i in a if "#" in set(i)]
a = list(zip(*a))

for i in a:
  print(*i,sep="")
  

# 駒を進めるときは、上限がn以下になるかで制御できる
n = int(input())
a = [int(input()) for _ in range(n)]

c = 1
s = a[0]

while s != 2 and c < n:
  c += 1
  s = a[s-1]

print(c if c<n else -1)

#配列二分法だそうです かんたん二分探索

import bisect

n,q = map(int,input().split())
a = sorted(list(map(int,input().split())))

# bisect_leftはソートされた配列aにxを挿入する場合、添字がどこに来るか？を返す
# 例えばケース1 a = {100 130 160} x = 120
# 添字1に挿入できる つまり x自身より上は2つあるので
# nからbisect.bisect_leftで返ってくる値を引くと答えになる
for i in range(q):
  x = int(input())
  print(n - bisect.bisect_left(a,x))
  
  
# aとbの最小公倍数は、aとbの積をaとbの最大公約数で割ると出る
# lcm(a,b) = a*b/(gcd(a,b))

import math
a,b = map(int,input().split())
 
print(a*b//(math.gcd(a,b)))



import functools

# 最小公倍数
# https://ictsr4.com/py/m0150.html
def lcm(a, b):
    r = a % b
    if r == 0:
        return a
    return a * lcm(b, r) // r
  
n, m = map(int, input().split())
a = list(map(int,input().split()))

# 公倍数の半分、ということは、最初に半分にしたものたちの公倍数を求めればよい
c = [i//2 for i in a]

# x = aを半分にした配列cの最小公倍数
x = functools.reduce(lcm, c)

# y = kまでの間にxはいつくあるか
# 個数だけみればよいので、シミュレーションは不要
y = m // x

# cの中に、最小公倍数と割った結果が偶数になるものがあったら、半公倍数は叶わないため0を出力し終了
for i in c:
  if (x//i) % 2 == 0:
    print(0)
    exit()

# 元の数列aの最小公倍数と重複しているものは、0.5をかけても公倍数とならないため半分に？ちょっと自信ない
# 偶奇関係なく//2の答えにしたいときは,+1したものに//2する
ans = (y+1)//2

print(ans)


# L-Rの増減のみ記録し、累積和する

d = int(input())
n = int(input())
a = [0]*(d+2)
for i in range(n):
  l,r = map(int,input().split())
  a[l] += 1
  a[r+1] -=1

# これ画期的すぎる
for i in range(1, d + 1):
  a[i] += a[i - 1]
  print(a[i])
  
# 順列から組み合わせの数を導くためには//2する
import collections

n = int(input())
a = list(map(int,input().split()))

c = collections.Counter(a)
ans = 0

# iの出現回数 * n-i（残りのものの数）で、ペアになる数を導ける
# ans // 2で順列⇨組み合わせ
for i in c:
  ans += c[i] * (n-c[i])
  
print(ans//2)

# 条件に合うi<jを探すときは、jを固定する
# 2つのペアを引き算したとき、200の倍数であるペアはいくつある？
# 個数を数える ときは使おう！
n = int(input())
a = list(map(int,input().split()))

cnt = [0]*202

# iを保管しながら、条件に合うjを探してansに足す
ans = 0
for i in range(n):
  x = a[i]%200
  ans += cnt[x]
  cnt[x] += 1
  
print(ans)




# heapq 優先度付きque
# 一番大きいaiに対して//2をし続けていく問題
import heapq

n,m = map(int,input().split())
a = list(map(lambda x: -int(x),input().split()))

# 配列aをヒープ化
heapq.heapify(a)

# m回、heapから取り出した最大を2で割って、heapに戻してる
for i in range(m):
  x = -heapq.heappop(a)
  heapq.heappush(a,-(x // 2))
  
print(-sum(a))


# 同じ問題 bisect 二分探索ライブラリ

import bisect

n,m = map(int,input().split())
a = sorted(list(map(int,input().split())))

# 一番大きい額のものを//2したらうれしい
# aはソートして、一番右が大きい状態になっている
# 一番大きい（一番右、おしりの）ものをとって、xに入れる
# xを//2して入れ直す（ソート順にちゃんとなる）
# を、m枚分やると、解決
while m:
  m -= 1
  x = a.pop()
  bisect.insort(a,x//2)

print(sum(a))


# 全ての数値の組み合わせで最大値を出す

import itertools

n = int(input())
a = sorted(list(map(int,input().split())),reverse=1)

b = [a[0],a[1],a[2]]

c = []
for i in itertools.permutations(b,3):
  x = ''.join([str(n) for n in i])
  c.append(int(x))
  
print(max(c))

# 別解
from itertools import permutations
n = int(input())
ans = 0
for s in permutations(sorted(map(int, input().split()))[-3:]):
    ans = max(ans, int("".join(map(str, s))))
print(ans)


'''
999 → 0
1,000 → 1
1,001 → 2
n+1するごとに1ずつ増える n-999
⇨1,000以上なら n - 999

999,999 → 999,000
1,000,000 → 999,002
1,000,001 → 999,004
1,000,002 → 999,006
n+1するごとに2ずつ増える。途中でnとansの大小関係が反転する（ここが怪しい）
つまり、n-998, n-997...と推移していく
⇨1,000,000以上なら n - (999 - (n - 1000000 + 1))

...ここまではあってるぽい

999,999,999 → 1,999,999,000
1,000,000,000 → 1,999,999,003 +999999003 997
1,000,000,001 → 1,999,999,006 +999999005 996
1,000,000,002 → 1,999,999,009 +999999002 995
n+1するごとに3ずつ増える
⇨1,000,000,000以上なら
n + ((n + 100000000) - (100000000 - 999))

⇨1,000,000,000,000以上なら (3*n) + 999

⇨1,000,000,000,000,000 は (4*n) + 999


'''

n = int(input())

ans = 0
if n >= 1000000000000000:
  ans = (4*n) + 999
elif n >= 1000000000000:
  ans = (3*n) + 999
elif n >= 1000000000:
  ans = (2*n) + 999
elif n >= 1000000:
  ans = n - (999 - (n - 1000000 + 1))
elif n >= 1000:
  ans = n - 999
  
print(ans)



# bit全探索

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