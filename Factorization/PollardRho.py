#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 14:52:34 2025

@author: cornelius
"""

"""

                                POLLARD RHO
            
            We want to factorize the number n
            
            1. Define a function to generate pseudo random numbers 
               f(x) = (x**2 + 1) mod n
               
            2. Set x to be a random number between 2 und n-1 and
               y to the same value as x
               
            3. Calculate f(x,n) and f(f(y,n),n)
            
            4. Determine the gcd of both numbers. If gcd = 1 or gcd = n
               set x to f(x,n) and y to f(f(y,n),n) and restart at step 3
               
               If gcd is something in between it is a prime factor


"""



# -----------------------------------------------------------------------
#                               IMPORTS   
# -----------------------------------------------------------------------

from math import gcd
from random import randint
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


def f(x,n):
    return (x**2 + 1) % n


def pollardRho(n):
    
    x = randint(2,n-1)
    y = x
    
    d = 1
    
    while d == 1:
        x = f(x,n)
        y = f(f(y,n),n)
        
        d = gcd(abs(x-y),n)
        
        if d == n:
            return None
        
    return d
    



# REPEATEDLY APPLIES POLLARD rho TO FIND ALL PRIME FACTORS
def factorizeRho(n):
    
    factors = []
    while n > 1:
        
        if is_prime(n):  
            factors.append(n)
            break
        
        factor = pollardRho(n)
   
        factors.append(factor)
        n = n // factor
        
    return factors


