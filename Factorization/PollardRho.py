#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 14:52:34 2025

@author: cornelius
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


