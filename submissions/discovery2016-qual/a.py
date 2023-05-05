w = int(input())

s = 'DiscoPresentsDiscoveryChannelProgrammingContest2016'

for i, d in enumerate(s):
  print(d, end='')
  if (i + 1) % w == 0:
    print()
    
if len(s) % w != 0:
  print()
