'''
誤読してた。既に裏のものは表にできないと思ってた…
！！！「裏返す」は裏を表にすることでもある！！！

さっきのだと0110や1100が-1になってしまう
「11」が連続していてかつk=2でも操作できるのはnが4以上のとき
「0110」→「1100」→「1001」→「0000」
 3 回      2回      1回
 
 あああああn=3
'''

def f(n,x):
  k = x.count("1")
  kk = x.count("11")
  if k%2 == 1:
    return -1
  elif kk == 1 and k == 2:
    if n == 4 and s == '0110':
      return 3
    elif n == 3:
      return -1
    else:
      return 2
  else:
    return k//2

t = int(input())
for i in range(t):
  n = int(input())
  s = input()
  print(f(n,s))
