from functools import lru_cache

n = int(input())

@lru_cache
def f(k):
  if k == 0:
    return 1
  else:
    k = f(int(k/2))+f(int(k/3))
    return k

print(f(n))
