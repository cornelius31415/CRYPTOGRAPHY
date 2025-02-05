#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 17:19:37 2025

@author: cornelius
"""

"""
                    PRIMITIVE ROOTS
            
            Let n be an integer. 
            Let G be the set of numbers relatively prime to n.
            G contains phi(n) elements (phi: Euler totient)
            If n is a prime than G = {1,2,3,...,p-1}
            
            G is a multiplicative group mod n
            Primitive root is element g of group for which
            every other element of the group is a power of g mod n
            
            g**1, g**2, ... , g**phi(n)
            
            Prime Numbers always have a primitive root
            
            gcd(g,n) = 1
            
"""
# -----------------------------------------------------------------------
#                                 IMPORTS   
# -----------------------------------------------------------------------

from math import sqrt,gcd
from random import choice

# -----------------------------------------------------------------------
#                              MATH FUNCTIONS   
# -----------------------------------------------------------------------


# NUMBERS RELATIVELY PRIME TO n
def relativelyPrime(n):
    
    relativePrime = []
    
    for i in range(1,n):
        if gcd(i,n) == 1:
            relativePrime.append(i)
    
    return relativePrime
    
# CHECK IF NUMBER IS PRIME
def is_prime(n):
    
    for i in range(2,int(sqrt(n)+1)):
        if n % i == 0:
            return False
        
    return True

# GENERATE LIST OF PRIMES SMALLER THAN n
def primes(n):
    
    primes = [i for i in range(2,n+1) if is_prime(i)]

    return primes



def generatePrime(Range):
    
    primeList = primes(Range)
    prime = choice(primeList)
    return prime


print(generatePrime(1000))


# -----------------------------------------------------------------------
#                           PRIMITIVE ROOTS   
# -----------------------------------------------------------------------


# determines the primitive root of a number n
def primitiveRoot(n):
    
    # original set
    relativePrime = relativelyPrime(n)
    
    for g in relativePrime:
        testList = [pow(g,i,n) for i in range(0,len(relativePrime))]
  
        if set(testList) ==  set(relativePrime):
            return g
        
    return False
    



























