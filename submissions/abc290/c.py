'''
盛大なる勘違いをしていた
これも勘違いではないことを祈って投げる

・kより下の数字が何種類ある？
・その中で 0,1...k - 1 の単調増加を満たす最大の個数はいくつ？
・うおおおおおおおおおおおおおおおお setがいけない？？？ そりゃそうだよ配列の長さだよ
'''

n, k = map(int, input().split())
a = set(map(int, input().split()))

a = list(a)
a.sort()

cnt = 0
i = 0

for i in range(len(a)):
    if i == a[i] and k > i:
      cnt += 1
    else:
      break

print(cnt)
