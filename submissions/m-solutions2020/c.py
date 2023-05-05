n,k = map(int,input().split())
a = list(map(int,input().split()))

# 掛け算の範囲を見る
# 次に範囲外になるものと、範囲内になるものを比べる
for i in range(k,n):
  print('Yes' if a[i-k] < a[i] else 'No')
