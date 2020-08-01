from functools import lru_cache
//usando memorização para tornar a recursão mais leve
@lru_cache(maxsize = 1000)
def fibonacci(n):
  if type(n) != int:
    raise TypeError('O valor deve ser um inteiro positivo')
  if n < 1:
    raise ValueError('O valor deve ser um inteiro positivo')  
  if n == 1:
    return 1
  elif n == 2:
      return 1
  elif n>2:
    return fibonacci(n-1)+fibonacci(n-2)
 
rs,sq=[],[]

for n in range(1,39):
  sq.append(fibonacci(n))
'''
convergence'''

for i in range(1,51):
  rs.append(fibonacci(i+1)/fibonacci(i))
