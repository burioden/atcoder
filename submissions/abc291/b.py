n = int(input())
a = sorted(list(map(int, input().split())))

ans = a[n:-n]
sum = sum(ans)
div = (5 * n) - (2 * n)

print("{:.5f}".format(sum / div))
