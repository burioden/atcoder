n = int(input())

def f(num):
  if num == 0:
    return 1
  else:
    return num * f(num-1)
    
print(f(n))
