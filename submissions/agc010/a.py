n = int(input())
a = list(map(int,input().split()))

print("YES" if sum(a)%2 == 0 else "NO")
