'''
シミュレーションしたらすごくふるいだった…
考え方はあっていたので、ふるいをライブラリに追加するぞい！
'''

n,m = map(int,input().split())
a = set(map(int,input().split()))

A = max(max(a),m) + 1

k = [1] * A
is_prime = [1] * A
p = []

for i in a:
  k[i] = 0

for i in range(2,A):
  if not is_prime[i]:
    continue
  for j in range(i*2,A,i):
    is_prime[j] = 0
    k[i] = k[i] and k[j]
  if not k[i]:
    p.append(i)
    
for i in p:
  for j in range(i*2,A,i):
    k[j] = k[j] and k[i]

ans = [1]

for i in range(2,m+1):
  if k[i]:
    ans.append(i)
    
print(len(ans))
for i in ans:
  print(i)
