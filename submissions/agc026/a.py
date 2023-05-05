n = int(input())
a = list(map(int,input().split()))

cnt = 0
x = 0
for i in range(1,n):
    if a[i-1] == a[i]:
        x += 1
    else:
        cnt = cnt + ((x+1)//2)
        x = 0
cnt = cnt + ((x+1)//2)
print(cnt)
