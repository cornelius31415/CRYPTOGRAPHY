#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 12:40:33 2025

@author: cornelius
"""

"""
                            SCENARIO
                A bank has e customers and wants to send a message m to
                all of them. It uses the different public keys of the
                customers n_i but always the same exponent e.

"""

import math
from MathFunctions import multiplicativeInverse



pubkeylist = [(143,3),(391,3),(899,3)]
cipherlist = [60,203,711]



def lowExponentAttack(pubkeylist,cipherlist):
    
    e = pubkeylist[0][1]
    nList = [pub[0] for pub in pubkeylist]
    n = 1
    for pub in nList:
        n *= pub 
        
    NList = [n/element for element in nList]
    yList = [multiplicativeInverse(NList[i], nList[i]) for i in range(len(nList)) ]
    factors = [cipherlist[i]*yList[i]*NList[i] for i in range(len(nList))]
    c = sum(factors)%n
    m = math.ceil(c**(1/e)) % n    
    
    return m
    
    
print(lowExponentAttack(pubkeylist, cipherlist))



