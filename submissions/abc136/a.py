a,b,c = map(int, input().split())
ans = c-(a-b)

print(0 if ans < 0 else ans)
