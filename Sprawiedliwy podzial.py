n = int(input())
bajtyna = input().split()
bitek = input().split()
  
bajtyna2 =[0]
bitek2 = [0]
answer = []
for i in range(n):
  if sum(bajtyna2) < sum(bitek2):
    answer.append(0)
    bajtyna2.append(int(bajtyna[i]))
  else:
    answer.append(1)
    bitek2.append(int(bitek[i]))
  
print(*answer)