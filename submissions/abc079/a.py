n = input()

ans = ''
if n[0] == n[1] == n[2]:
  ans = 'Yes'  
elif n[1] == n[2] == n[3]:
  ans = 'Yes'
else:
  ans = 'No'
  
print(ans)
