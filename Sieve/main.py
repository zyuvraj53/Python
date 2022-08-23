from math import isqrt # isqrt is integer sqrt of the number

def primes_less_than(n:long4) -> list[long4]:
  if n<=2:
    return []
  is_prime = [True] * n
  is_prime[0] = False
  is_prime[1] = False
  
  # for i in range(2, n): We don't need to check up all the way upto n, since one of the factors must be sqrt(n)
  for i in range(2, isqrt(n)):
    if is_prime[i]:
      for x in range(i*i, n, i):
        is_prime[x] = False
  
  return [i for i in range(n) if is_prime[i]]
    

if __name__=='__main__':
  print(primes_less_than(100000)) 