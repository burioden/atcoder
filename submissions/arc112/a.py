'''
x = R-Lとする R-x = L
R-L = x 〜 R-x = L の個数は(x-L)+1で求められる
↑を最大範囲として、最小の範囲は x-L = L の1つ
最大範囲から最小範囲まで、個数は1ずつ減っていくので
1...(x-L)+1を足せば答えは出そう？

(x-L)がマイナスったら0

L=Rのときは、0のみ1、他は0
'''
tora = int(input())
for inu in range(tora):
  l,r = map(int,input().split())
  if r == l:
    if r == 0:
      print(1)
    else:
      print(0)
  elif (r-l) - l < 0:
    print(0)
  else:
    OxO = (r-l)-l+1
    print(((OxO+1)*OxO)//2)
  
