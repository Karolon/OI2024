import sys
n = input()
sys.set_int_max_str_digits(0)
amount = 0
while True:
  '''  if not('2' in n or '3' in n or '4' in n or '5' in n or '6' in n or '7' in n or '8' in n or '9' in n):
      if n.count('1') == 1:
        break'''
  if n[-1] == '9' or n[-1] == '0':
    n+=n[0]
    n = n[1:]
    n=str(int(n))
    amount+=1
  elif n != '1':
    while n[-1] != '9':
      n = str(int(n)+1)
      amount+=1
  if not('2' in n or '3' in n or '4' in n or '5' in n or '6' in n or '7' in n or '8' in n or '1' in n or '0' in n) or n == '1':
    break

  
if len(n) != 1:
  n = str(int(n)+1)
  amount+=1
  n+=n[0]
  n = n[1:]
  n=str(int(n))
  amount+=1
print(n)

print(amount)
while True:
  pass