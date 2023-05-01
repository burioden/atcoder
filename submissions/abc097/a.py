a,b,c,x = map(int, input().split())

def ans():
  ab = abs(a-b)
  ac = abs(a-c)
  bc = abs(b-c)

  if ab <= x and bc <= x:
    return "Yes"
  if ac <= x:
    return "Yes"
  
  return "No"

print(ans())
