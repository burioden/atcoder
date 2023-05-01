n,x = map(int, input().split())
li= [int(input()) for _ in range(n)]

ans = x-sum(li)

print((ans//min(li))+n)
