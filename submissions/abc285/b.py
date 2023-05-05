'''
解説読んでも動画見てもわからなさすぎた
s[i] == s[i+1]になったら打ち止め、がわからなさすぎ
コード拝見してはじめてわかった くうう
'''

n = int(input())
s = input()

for i in range(1,n):
  l = 0
  while l + i < n and s[l] != s[l+i]:
    l += 1
  print(l)
