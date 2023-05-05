a = int(input())
b = int(input())

ans = max(a,b)-min(a,b)
ans_s = 10-(max(a,b))+(min(a,b))

print(min(ans,ans_s))
