a,b = map(int,input().split())

if a<0 and b<0:
  if (a+b)% 2 == 0:
    print("Negative")
  else:
    print("Positive")
elif 0<a and 0<b:
  print("Positive")
else:
  print("Zero")
