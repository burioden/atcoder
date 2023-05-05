n = int(input())

'''
t = 動く総回数
x = ヨコに動かなきゃいけない回数
y = タテに動かなきゃいけない回数

・tは絶対に昇順
・x+y と t の偶奇は揃ってないと行けない
・t = 偶数であれば出発点にも戻れる , 奇数であれば戻れない

例えば t = 2 , x = 0 , y = 1 : t = 偶 , x+y = 奇
つまり 2+0+1 = 3 は、明らかに行けない

①t+x+yが奇数なら行けない
②前いたところからの距離より、tが大きかったら行けない

'''
# 前にいたところと前のタイム保管用
bt,bx,by = 0,0,0

flg = 1
for i in range(n):
  t,x,y = map(int, input().split())
  if (x+y+t) % 2 == 1:
    flg = 0
    break
  elif t-bt < abs(x-bx) + abs(y-by):
    flg = 0
    break
  bt,bx,by = t,x,y
  
print('Yes' if flg else 'No')
