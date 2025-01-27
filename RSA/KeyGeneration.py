#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 11:58:30 2025

@author: cornelius
"""

"""
                            KEY GENERATION
                            
                1. PUBLIC KEY
                
                    1.  Choose 2 prime numbers p and q
                    2.  Multiply them n = pq
                    3.  Calculate     m = (p-1)(q-1)
                    4.  Find a number e such that gcd(e,m) = 1
                    5.  Public Key is tupel (n,e)
                
                
                
                
                2. PRIVATE KEY
                
                    1. You need the public key (n,e) and the 2 primes p,q
                    2. Calcualte the multiplicative inverse d of e mod m -> 
                         de = 1 mod m
                    3. Private Key is tuple (n,d)


"""


# -----------------------------------------------------------------------------
#                                   IMPORTS
# -----------------------------------------------------------------------------


from math import gcd
from MathFunctions import multiplicativeInverse



# -----------------------------------------------------------------------------
#                            PUBLIC KEY GENERATION
# -----------------------------------------------------------------------------


def publicKeyGeneration(p,q):
    n = p*q
    m = (p-1)*(q-1)
    e = 0
    for i in range(25,m):
        if gcd(i,m)==1:
            e = i
            break
    pub = (n,e)    
    return pub


# -----------------------------------------------------------------------------
#                            PRIVATE KEY GENERATION
# -----------------------------------------------------------------------------


def privateKeyGeneration(p,q,pub):
    e = pub[1]
    m = (p-1)*(q-1)
    d = multiplicativeInverse(e,m) # multiplicative inverse of e mod m
    # d = pow(e,-1,m)              # multiplicative inverse also possible with pow()-function
    priv = (pub[0],int(d))
    return priv



# -----------------------------------------------------------------------------
#                                   TESTING
# -----------------------------------------------------------------------------


# pub = publicKeyGeneration(31, 37)
# priv = privateKeyGeneration(31, 37, pub)
# print(pub)
# print(priv)