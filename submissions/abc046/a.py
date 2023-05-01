a,b,c = map(int, input().split())

if a==b==c:
  print(1)
elif not a==b and not a==c and not b==c:
  print(3)
else:
  print(2)
