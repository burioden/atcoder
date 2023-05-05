n = int(input())
ans = ""

if n == 100:
  ans = "Perfect"
elif 90 <= n:
  ans = "Great"
elif 60 <= n:
  ans = "Good"
elif n <= 59:
  ans = "Bad"

print(ans)
