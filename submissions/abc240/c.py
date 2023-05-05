'''
DPだなあ、はわかったけれど、漸化式が立てられなかったし、実装わかんなかった…

で、これが噂のbitDP…？パワフルすぎん…？？
ふつうにdpやると

・sample1
0001001 -> 00010011011
x = 10に1が経ってるからOK

それをbitにすると逆にはなるけど、x桁めに1が立ってればYes
来た道は見る必要はないので、1001000 -> 110110000000 に変更されてもOK

やば…
'''

n, x = map(int, input().split())
jump = [list(map(int,  input().split())) for _ in range(n)]

dp = 1

for i in range(n):
  dp = (dp << jump[i][0]) | (dp << jump[i][1])
  # print(bin(dp), bin(dp << jump[i][0]), bin((dp << jump[i][1])))
  
if (dp >> x) & 1 == 1:
  print('Yes')
else:
  print('No')
