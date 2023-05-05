h,w = map(int,input().split())
li = []
for i in range(h):
  s = input()
  li.append(s)

print("#"*(w+2))
for i in li:
  print("#"+i+"#")
print("#"*(w+2))
