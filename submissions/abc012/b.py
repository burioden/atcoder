n = int(input())

h = str(n//60//60%60).zfill(2)
m = str(n//60%60).zfill(2)
s = str(n%60).zfill(2)

print(h+":"+m+":"+s)
