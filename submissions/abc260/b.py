n,x,y,z = map(int, input().split())
aa = list(map(int,input().split()))
bb = list(map(int,input().split()))

# 合格者は x + y + z (< n) 人
# 点数を負の数にしてあげると、符号は無視して[大きい点数順,小さい番号順]に並べてくれる
# 例えば 80,3と 80,1 を普通にソートすると[[80,3],[80,1]]になってしまうが
# 点数を負にすることにより [[-80,1],[-80,3]] と逆転す
# 理由はたぶん[-80+1 = -79]と[-80+3 = -77]として解釈されるから？

# aaの(-点数,番号) の(-点数)もとにaaをソートしたものの番号リストを作る 
st = sorted([i for i in range(n)], key=lambda j: (-aa[j],j))
# ソートしたものの上からxまでをansに入れる
ans = st[:x]

# さっき作ったものx番目以降の配列を bbの(-点数,番号) をもとにソート  
st = sorted(st[x:],key=lambda j: (-bb[j],j))
ans += st[:y]

# さっき作ったものy番目以降の配列を bbとaaの(-点数,番号)合計 をもとにソート  
st = sorted(st[y:],key=lambda j: (-aa[j] - bb[j],j))
ans += st[:z]

# ソートしたansの中身を+1しながら出力
for i in sorted(ans):
  print(i + 1)
