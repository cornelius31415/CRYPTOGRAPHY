#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 11:58:30 2025

@author: cornelius
"""

from math import gcd
from MathFunctions import multiplicativeInverse


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

def privateKeyGeneration(p,q,pub):
    e = pub[1]
    m = (p-1)*(q-1)
    d = multiplicativeInverse(e,m) # multiplicative inverse of e mod m
    # d = pow(e,-1,m) # multiplicative inverse also possible with pow()-function
    priv = (pub[0],int(d))
    return priv



pub = publicKeyGeneration(31, 37)
priv = privateKeyGeneration(31, 37, pub)
print(pub)
print(priv)