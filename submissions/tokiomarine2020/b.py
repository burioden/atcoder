'''
そうか、aよりもbが前にいることばかり考えていた
'''

a, v = map(int, input().split())
b, w = map(int, input().split())
t = int(input())

if a + v * t < b + w * t or a - v * t > b - w * t:
  print('NO')
else:
  print('YES')
