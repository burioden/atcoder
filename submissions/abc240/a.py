a, b = map(int, input().split())

ans = ''

if abs(a - b) == 1:
  ans = 'Yes'
elif a == 1 and b == 10:
  ans = 'Yes'
elif a == 10 and b == 1:
  ans = 'Yes'
else:
  ans = 'No'
  
print(ans)
