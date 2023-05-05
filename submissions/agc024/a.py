a,b,c,k = map(int, input().split())

if abs(a-b) > 10**18:
  print("Unfair")
elif k%2 == 0:
  print(a-b)
elif k%2 == 1:
  print(b-a)
