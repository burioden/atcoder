n = int(input())
w = list(input().split())
a = ["and", "not", "that", "the", "you"]

for i in w:
  if i in a:
    exit(print('Yes'))
    
print('No')
