n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
b = [list(map(int, input().split())) for _ in range(n)]

for _ in range(4):
  # [::-1]で逆からにしたものを、行と列反転させると90度回転になる！アア！！
  a = list(zip(*a[::-1]))
  # ひとつでもtrueならばOK elseを設定しないのがコツだ ほぉん
  if all(a[i][j] <= b[i][j] for i in range(n) for j in range(n)):
    exit(print('Yes'))

print('No')
