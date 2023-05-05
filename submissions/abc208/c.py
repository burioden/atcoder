import operator

n,k = map(int,input().split())
a = list(map(int,input().split()))

# 均等に配れるお菓子
x = k//n
# 余っちゃうお菓子
y = k%n

#aの人たちをb[i][0]に、配った均等おかしを[i][1]に入れる
b = []
for i in range(n):
  b.append([i,a[i],x])
  
# 国民番号順にソートして、配る
for i in sorted(b,key=operator.itemgetter(1)):
  if y > 0:
    y -= 1
    i[2] += 1
  else:
    break

for i in range(n):
  print(b[i][2])
