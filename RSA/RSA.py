#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 12:09:43 2025

@author: cornelius
"""

"""
                            RSA CRYPTOGRAPHY
            
            1. ENCRYPTION
                
                1. Get n and e from the public key
                2. Get the ASCII-code for every char in the plaintext
                3. Calculate the modular exponent y = ord(char) ** e mod n
                   for every char in the plaintext
                4. Return a list of numbers where each number stands for
                   an encrypted char
            
            
            2. DECRYPTION
            
                1. Get n and d from the private key
                2. For every number in the encrypted message calculate the
                   modular exponent x = number ** d mod n
                3. Each x is the ASCII-code of a letter -> Apply chr()
                4. Join all x together in a string -> original message
            
"""

# -----------------------------------------------------------------------------
#                                 IMPORTS
# -----------------------------------------------------------------------------

from MathFunctions import fastModularExponent 
from KeyGeneration import publicKeyGeneration, privateKeyGeneration


# -----------------------------------------------------------------------------
#                                  SETUP
# -----------------------------------------------------------------------------

message = "i love you"

public = publicKeyGeneration(31, 37)
private = privateKeyGeneration(31, 37, public)


# -----------------------------------------------------------------------------
#                               ENCRYPTION
# -----------------------------------------------------------------------------


def encrypt(plaintext,publicKey):
    
    n = publicKey[0]
    e = publicKey[1]
    
    encryptedMessage = []
    
    for char in plaintext:
        y = fastModularExponent(ord(char), e, n)
        #y = pow(ord(char),e,n)         # python internal function
        encryptedMessage.append(y)
        
    return encryptedMessage





# -----------------------------------------------------------------------------
#                              DECRYPTION
# -----------------------------------------------------------------------------


def decrypt(secret,privateKey):
    
    n = privateKey[0]
    d = privateKey[1]
    
    decryptedMessage = ""
    
    for number in secret:
        x = fastModularExponent(number, d, n)
        #x = pow(number,d,n)         # python internal function
        decryptedMessage += chr(x)
    return decryptedMessage



# -----------------------------------------------------------------------------
#                               TESTING
# -----------------------------------------------------------------------------
print()
print("------------   RSA Encryption Test   ------------ ")
print()

secret = encrypt(message, public)
print("Encrypted Message: ",secret)
print()
message = decrypt(secret, private)
print("Original Message: ",message)
















