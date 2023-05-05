n = int(input())

if len(str(n)) == 1:
  print('AGC00',n,sep='')
elif n >= 42:
  print('AGC0',n+1,sep='')
else:
  print('AGC0',n,sep='')
