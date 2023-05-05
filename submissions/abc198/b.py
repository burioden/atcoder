n = input()[::-1]

x = 0
for i in n:
  if i == "0":
    x += 1
  else:
    break

s = n+"0"*x
s = s[::-1]
N = s[::-1]

print('Yes' if s==N else 'No')
