a = [int(input())for i in[0]*3]

for x in a:
  print(3-sorted(a).index(x))
