s = list(input().split())
t = list(input().split())

a = [['R','G','B'],['G','B','R'],['B','R','G']]

if s in a and t in a:
  print('Yes')
elif s not in a and t not in a:
  print('Yes')
else:
  print('No')
