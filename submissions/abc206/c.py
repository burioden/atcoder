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
