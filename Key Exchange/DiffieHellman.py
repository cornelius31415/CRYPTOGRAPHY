#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 16:52:10 2025

@author: cornelius
"""

"""

Alice und Bob einigen sich auf:
    - eine Primzahl p 
    - eine Primitivwurzel g modulo p in Z_p

Primzahl und Primitivwurzel können öffentlich bekannt sein

Part-Key Alice
Alice wählt eine natürliche Zahl a in {1,2,...,p-2} zufällig
Alice berechnet A = g**a mod p
Alice schickt A an Bob und hält a geheim

Part-Key Bob
Bob wählt eine natürliche Zahl b in {1,2,...,p-2} zufällig
Bob berechnet B = g**b mod p
Bob schickt B an Alice und hält b geheim

Der Schlüssel ist K = g**(ab) mod p
Für Bob heißt das K = A**b mod p
Für Alice dann    K = B**a mod p



"""

from PrimitiveRoot import primitiveRoot, generatePrime
from random import randint


# Step 1: Generate prime number p
# Step 2: Determine primitve root of p
# Step 3: Calculate the Part-Key
# Step 4: Calculate the Key


p = generatePrime(int(1e4))
g = primitiveRoot(p)

def partKey(p,g):
    
    a = randint(0, p-1)
    A = pow(g, a, p)
    return (A,a)
    




def Key(part_key,exponent):
    
    key = pow(part_key[0], exponent,p)
    return key
    
p = 17
g = primitiveRoot(p)

print(partKey(p,g))


































