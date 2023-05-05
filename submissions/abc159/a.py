'''
nから2つ、またはmから2つ選ぶ方法でないと、偶数にはならぬ
組み合わせのパターンはnC2 + mC2、になる
'''
import math

n, m = map(int, input().split())

print(math.comb(n, 2) + math.comb(m, 2))
