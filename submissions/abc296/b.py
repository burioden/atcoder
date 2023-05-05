g = [input() for _ in range(8)]
d2 = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h'}
d = {7: '1', 6: '2', 5: '3', 4: '4', 3: '5', 2: '6', 1: '7', 0: '8'}

for i in range(8):
  for j in range(8):
    if g[i][j] == '*':
      print(d2[j], d[i], sep='')
