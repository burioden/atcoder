'''
・1,2,3...の順列と差異があるところのインデックス + 1を格納する
・ペアで足し算していき、k以上のものがあればNo、なければYes
  これ、全部違った場合にTLEになる？ならなかった
  ので、両端から足していく
  
・そもそも。n < kであれば、入れ替えられる
  入れ替えるコストの最大は1とNなので、1 + Nになる
・そうでない n >= k場合のみ見るべき

と考えるとどうでしょう

'''

n, k = map(int, input().split())
p = list(map(int, input().split()))

if n < k:
  exit(print('Yes'))

for i, d in enumerate(p):
  if i + 1 != d and i + 1 >= k:
    exit(print('No'))
    
print('Yes')
