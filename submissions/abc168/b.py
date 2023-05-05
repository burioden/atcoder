k = int(input())
s = input()

if k < len(s):
  print(s[:k]+"...")
else:
  print(s)
