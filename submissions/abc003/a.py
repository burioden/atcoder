n = int(input())
yen = 0
for i in range(1,n+1):
  yen += i * 10000

print(yen//n)
