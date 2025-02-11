#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 14:26:08 2025

@author: cornelius
"""


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

# FIND PRIME FACTORS BY TRIAL DIVISION
def factorizeBruteForce(n):
    
    factors = []
    num = n
    for factor in primes(int(n**0.5)+1):
        while num % factor == 0:
            factors.append(factor)
            num = num // factor
    
        if num == 1:
            break
    
    if num > 1:
        factors.append(num)
          
    return factors