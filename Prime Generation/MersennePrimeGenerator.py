#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 09:05:55 2025

@author: cornelius
"""


# -----------------------------------------------------------------------
#                               IMPORTS  
# -----------------------------------------------------------------------

import time 
import MillerRabin

# -----------------------------------------------------------------------
#                            PRIME NUMBERS   
# -----------------------------------------------------------------------


# SIMPLE CHECK IF n IS PRIME
def is_prime(n):
    
    for i in range(2,int((n**0.5)+1)):
        if n % i == 0:
            return False
    
    return True





# GENERATES MERSENNE PRIMES using Miller Rabin Test (MR) 
def mersennePrime(amount):
    
    # Mersenne Primzahl: 2**k - 1 
    
    mersenne_primes = []
    
    start = time.time()
    
    k = 2
    while len(mersenne_primes) < amount:
        
        mersenne = (2**k) -1
        if MillerRabin.primeTest(mersenne) == True:
            mersenne_primes.append((mersenne,k))
            
            binaryMersenne = bin(mersenne)[2:]
            bitLength = len(binaryMersenne)
            
            end = time.time()
            runtime = end-start
            
            print("                                   ------------------")
            print(f"                                   {len(mersenne_primes)}. Mersenne Prime")
            print("                                   ------------------")
            print("")
            
            print(f"{mersenne}")
            print("")
            print(f"Runtime: {runtime:.6f} s")
            print(f"k = {k}")
            print(f"Bit Length: {bitLength}")
        
        k += 1
        
    
    return mersenne_primes








# -----------------------------------------------------------------------
#                                TESTING   
# -----------------------------------------------------------------------


    

print("--------------------------------------------------------------------------------------")
print("                                    MERSENNE PRIMES")
print("--------------------------------------------------------------------------------------")
print("")
print("                             Primes of the form 2**k - 1")
print("                             Primality checked with Miller Rabin")
print("")


mersennePrime(15)




