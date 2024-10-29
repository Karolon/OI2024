n = int(input())
robots = []
s_max =[0,0]
z_max = [0,0]

for i in range(n):
  s,z = input().split()
  s,z = int(s),int(z)
  robots.append([s,z])
  if s_max[0] > s:
    s_max = [s,z]
  if z_max[1] > z:
    z_max = [s,z]
    
if s_max == z_max:
  print('NIE')
#jeżeli liczba robotów które mogą wygrać siłą == liczba robotów które mogą wygrać zręczniścią