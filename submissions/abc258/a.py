k = int(input())

h = str(21 + (k//60))
m = str(k%60)

if len(m) == 1:
  m = '0'+m
  
print(h,':',m,sep="")
