a,b,c,d = map(int, input().split())

ans = min(b,d)-max(a,c)

print('Yes' if -1 < ans else 'No')
