h,w = map(int, input().split())
a = [input().split() for i in range(h)]

coll=""

for i in range(w):
  for item in a:
    coll += item[i] + " "
  print(coll)
  coll = ""
