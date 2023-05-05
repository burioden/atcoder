'''
実装が下手〜〜〜〜〜〜〜
'''

def f(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])
    if temp!=1:
        arr.append([temp, 1])
    if arr==[]:
        arr.append([n, 1])
    return arr

n = int(input())
a = f(n)

cnt = 0

for i, d in a:
  now = 1
  while d - now >= 0 and n > 1:
    d -= now
    cnt += 1
    n //= (i**now)
    now += 1
    
print(cnt)
