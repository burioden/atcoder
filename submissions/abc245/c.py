'''
前はaの配列にいるか、bの配列にいるか、をちゃんと見よう
今だけではなく、ひとつ前も見よう…
あとひとつ、a[i]から他の配列の(b[i - 1])を見るとき
absの取り方も、iを固定して気をつけてみてね!!
'''

n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ans = [True, True]

for i in range(1, n):
  a1 = (abs(a[i - 1] - a[i]) <= k) and ans[0]
  a2 = (abs(b[i - 1] - a[i]) <= k) and ans[1]
  b1 = (abs(a[i - 1] - b[i]) <= k) and ans[0]
  b2 = (abs(b[i - 1] - b[i]) <= k) and ans[1]
  
  ans[0] = a1 or a2
  ans[1] = b1 or b2

print('Yes' if ans[0] or ans[1] else 'No')
