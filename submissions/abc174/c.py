k = int(input())

x = 7

# k = 7 か 1なら1回でfin. kが偶数ならむり
if k == 7 or k == 1:
  print(1)
  exit()
elif k%2 == 0:
  print(-1)
  exit()

# その他は、実際にx = 7を 77,777,777...と増やしていき、x = 777... を kで割ったあまりが0になったらOK
# 77が1項目になっちゃってるから、i+1で出力
for i in range(1,10**6):
  x = x*10 + 7
  x %= k
  if x == 0:
    print(i+1)
    exit()
    
print(-1)
