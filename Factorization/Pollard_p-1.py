#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 18:29:29 2025

@author: cornelius
"""

"""
                                POLLARD p-1 FACTORIZATION
                        
            Let n be the number we want to factorize and p one of its prime factors
            
            According to Fermat's little theorem 2**(p-1) = 1 mod p
            
            This means that p divides 2**(p-1) - 1
            
            But p also divides 2**k - 1 with k being a multiple of p-1
            
            If we find a multiple k of p-1 we can
            
            1. calculate 2**k - 1 and then
            2. calculate gcd(2**k - 1, n)
            
            The gcd will be the prime factor p.
            
            
            THE ALGORITHM
            
            1. Set a boundary H. H should not be too big, otherwise n will be a gcd. 
            2. Calculate all prime numbers smaller than H
            3. For each prime calculate the highest power smaller than H
            4. Multiply all the prime powers together -> multiple of p-1
            5. Calculate 2**k - 1 mod n
            6. Calculate gcd(2**k-1 mod n, n)
            
            
            



"""

# -----------------------------------------------------------------------
#                               IMPORTS   
# -----------------------------------------------------------------------

from math import gcd
import time

# -----------------------------------------------------------------------
#                            PRIME SECTION   
# -----------------------------------------------------------------------

# CHECK IF NUMBER IS PRIME
def is_prime(n):
    
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
        
    return True

# GENERATE LIST OF PRIMES SMALLER THAN n
def primes(n):
    
    primes = [i for i in range(2,n+1) if is_prime(i)]

    return primes


def factorizeBruteForce(n):
    
    factors = []
    num = n
    for factor in primes(int(n**0.5)):
        while num % factor == 0:
            factors.append(factor)
            num = num / factor
    
        if num == 1:
            break
          
    return factors

# -----------------------------------------------------------------------
#                             POLLARD p-1   
# -----------------------------------------------------------------------

# HIGHEST PRIME POWER SMALLER THAN BOUNDARY H
def highestPower(p,H):
    
    hPower = p
    
    while hPower*p <=   H :
        hPower *= p
        
    return hPower
    
# CALCULATE A MULTIPLE OF p-1
def multipleK(H):
    
    primeProduct = 1
    
    for prime in primes(H):
        primeProduct *= highestPower(prime, H)
                
    return primeProduct
    
# THE ACTUAL POLLARD p-1 FACTORIZATION
def pollardFactorize(n):
    
    H = min(int(n**0.25),100000)
    
    k = multipleK(H)
    factor = gcd(pow(2,k,n)-1,n)
    
    return factor



# -----------------------------------------------------------------------
#                               TESTING   
# -----------------------------------------------------------------------

n = 1372319802547       #    = 174440041*7867


#                       Brute Force Factorization

start1 = time.time()

primeFactor = factorizeBruteForce(n)[0]

end1 = time.time()
runtime1 = end1 - start1

print(f"\nBrute Force Factor: {primeFactor}")
print(f"Brute Force Factorization Runtime:{runtime1: .4f}s \n")




#                       Pollard p-1 Factorization

start2 = time.time()

primeFactor = pollardFactorize(n)

end2 = time.time()
runtime2 = end2 - start2

print(f"Pollard p-1 Factor: {primeFactor}")
print(f"Pollard p-1 Runtime:              {runtime2: .8f}s")
    

print(f"Pollard Algorithm is {round(runtime1/runtime2,1)} times faster than the Brute Force Algorithm")




    
    
    

