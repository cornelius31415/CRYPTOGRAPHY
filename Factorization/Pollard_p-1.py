#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 18:29:29 2025

@author: cornelius
"""

from math import sqrt, log, floor

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




def pollardFactorization(n):
    
    B = sqrt(n)
    
    k = 2
    for prime in primes(B):
        k *= floor(log(B,prime))
        
    if 
    
    
    
    
    pass