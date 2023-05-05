x, y = map(int, input().split())
k = int(input())

omote = x
while y > 0 and k > 0:
  y -= 1
  k -= 1
  omote += 1

print(omote - k)
