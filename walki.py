n = int(input())
robots = []
s_max =[0,0]
z_max = [0,0]
sz = 0

for i in range(n):
  s,z = input().split()
  s,z = int(s),int(z)
  robots.append([s,z])
  if s_max[0] > s:
    s_max = [s,z]
  if z_max[1] > z:
    z_max = [s,z]
  if s == z:
    sz +=1
    
if robots.index(s_max) == robots.index(z_max):
  print('NIE')
elif len(robots) % 2 == sz % 2:  # jeżeli jest nieparzysta ilość robotów  i nieparzysta ilość robótów u kturych s == z to NIE (jeżli obie są ilości są parzyste to można usunąć jednego robota z s == z i zmienić je na nieparzyste)
  print('NIE')



#jeżeli jest robot s==z to zawsze da się doprowadzić do tego żeby było jeden robot gdzie s == z
#\tak wtedy gdy ilość jest parzysta i nigdzie z != s oraz w wszystkich przypadkach które są w stanie do tego doprowadzić
#\jeżeli jest pażyste to znajdzie się tak możliwość(chyba że istnieje s == z)
#co jeżeli liczba robotów jest nieparzysta gdzie nie ma s==z?
#-





  
#jeżeli liczba robotów które mogą wygrać siłą == liczba robotów które mogą wygrać zręczniścią