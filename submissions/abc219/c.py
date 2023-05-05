'''
xを数字とセットにした二次元配列を作る
sを数字に置き換えたものと、元のままのものの三次元配列にする
→二次元配列では取り扱いきれないので、遠慮なく三次元へ
ソートして、出す
'''
from collections import defaultdict

x = input()
n = int(input())
s = [input() for _ in range(n)]

new = defaultdict(dict)

for i in range(len(x)):
  new[x[i]] = i

ans = []

for i in s:
  inner = []
  for j in i:
    inner.append(new[j])
  ans.append([inner, i])

ans.sort()

for i in ans:
  print(i[-1])
