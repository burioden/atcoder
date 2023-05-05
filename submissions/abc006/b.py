n = int(input())

# 10^5と3^2の配列を作っておく
l = [0 for _ in range(1000009)]
l[0],l[1],l[2] = 0,0,1

# 配列の値を書き換える時、100007で割った答えを格納しておく
for i in range(3,1000009):
  l[i] = ((l[i-1]+l[i-2]+l[i-3])%10007)

print(l[n-1])