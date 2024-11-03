n,m,k = input().split()
n,m,k = int(n), int(m), int(k)
stare = []#bitada
nowe = []#bajtogród
liczba = 0

for _ in range(n-1):
  x,y = input().split()
  stare.append([int(x), int(y)])
  
for _ in range(m-1):
  x,y = input().split()
  x,y=int(x), int(y)
  nowe.append([min(x,y),max(x,y)])


for _ 
  stare_alt = []
  for i in range(n):
    for j in range(m):
      for l in range(n-1):
        x,y = stare[l][0], stare[l][1]
        if x == i:
          x = j
        if y == i:
          y = j
        stare_alt.append([min(x,y),max(x,y)])
  if stare_alt == nowe:
    liczba+=1
    
print(liczba)