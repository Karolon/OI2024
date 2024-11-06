from kaslib import DajN, Pytaj, Szturchnij, Odpowiedz

def is_prime(x):
  if x <= 3:
    return True
  else:
    for i in range(5,x//2+1,2):
      if x % i == 0:
        return False
    return True


dzielniki = []
x = 0
n = DajN()
for x in range(2,n):
  if is_prime(x):
    nwd = Pytaj(x)
    if not nwd in dzielniki:
      dzielniki.append(nwd)
print(max(dzielniki))