#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 09:05:55 2025

@author: cornelius
"""
"""
effizienter machen durch: numpyArray,
ziel: zu sehen wie lange es dauert jede perfekte zahl zu berechnen
n-te perfekte zahl braucht n-te mersenne primzahl
mersenne primzahl ist
"""


# -----------------------------------------------------------------------
#                               IMPORTS  
# -----------------------------------------------------------------------

import time 
import MillerRabin

# -----------------------------------------------------------------------
#                            PRIME NUMBERS   
# -----------------------------------------------------------------------


# CHECK IF n IS PRIME
def is_prime(n):
    
    for i in range(2,int((n**0.5)+1)):
        if n % i == 0:
            return False
    
    return True


# CREATES A LIST OF amount  PRIMES
def primeList(amount):
    
    primes = []
    
    i = 0
    l = 2
    while i < amount:
        if is_prime(l):
            primes.append(l)
            i+=1
        l += 1
    
    return primes




# GENERATES MERSENNE PRIMES using Miller Rabin Test (MR) and Bitshift (BS)
def mersennePrimeMRBS(amount):
    
    # Mersenne Primzahl: 2**k - 1 
    
    mersenne_primes = []
    
    k = 2
    while len(mersenne_primes) < amount:
        
        mersenne = (1<<k) -1
        if MillerRabin.primeTest(mersenne) == True:
            mersenne_primes.append((mersenne,k))
        
        k += 1
        
    
    return mersenne_primes

# GENERATES MERSENNE PRIMES using Miller Rabin Test (MR) 
def mersennePrimeMR(amount):
    
    # Mersenne Primzahl: 2**k - 1 
    
    mersenne_primes = []
    
    k = 2
    while len(mersenne_primes) < amount:
        
        mersenne = (2**k) -1
        if MillerRabin.primeTest(mersenne) == True:
            mersenne_primes.append((mersenne,k))
        
        k += 1
        
    
    return mersenne_primes




# # -----------------------------------------------------------------------
# #                            PERFECT NUMBERS   
# # -----------------------------------------------------------------------

# # generates a certain amount of perfect numbers
# def perfekte_zahlen(amount):
    
#     start = time.time()
    
#     mersennes = mersennePrime(amount)
    
#     for element in mersennes:
#         k = element[1]
#         mersenne = element[0]
        
#         perfect = power_of_two(k-1)*mersenne
        
#         end_i = time.time()
#         runtime_i = end_i - start
        
#         print(f"Perfekte Zahl: {perfect}   Laufzeit: {runtime_i} s")
        
        
    
#     return perfect
    


# -----------------------------------------------------------------------
#                                TESTING   
# -----------------------------------------------------------------------

# MERSENNE PRIMES WITHOUT KNOWING PRIMES BEFORE

print("--------------------------------------------------------------------------------------")
print("                                   MERSENNE PRIMES")
print("--------------------------------------------------------------------------------------")
print("")
print("                                  Miller Rabin Test")
print("                                     Bit Shift")
print("")

start = time.time()

for i in range(1,14):
    
    mersenne_prime = mersennePrimeMRBS(i)
    
    end_i = time.time()
    runtime_i = end_i - start
    
    mPrime = str(mersenne_prime[-1][0])
    k = str(mersenne_prime[-1][1])
    
    print(f"{i:<2}:   {mPrime:<60}  Runtime: {runtime_i:.6f} s")
    

print("--------------------------------------------------------------------------------------")
print("                                   MERSENNE PRIMES")
print("--------------------------------------------------------------------------------------")
print("")
print("                                  Miller Rabin Test")
print("")

start = time.time()

for i in range(1,14):
    
    mersenne_prime = mersennePrimeMR(i)
    
    end_i = time.time()
    runtime_i = end_i - start
    
    mPrime = str(mersenne_prime[-1][0])
    k = str(mersenne_prime[-1][1])
    
    print(f"{i:<2}:   {mPrime:<60}  Runtime: {runtime_i:.6f} s")






