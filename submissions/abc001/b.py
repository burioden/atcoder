def f(m):
  if m < 100:
    return "00"
  elif m <= 5000:
    return str(m // 100).zfill(2)
  elif m <= 30000:
    return str(m // 1000 + 50)
  elif m <= 70000:
    return str((m // 1000 - 30) // 5 + 80)
  else:
    return "89"

print(f(int(input())))
