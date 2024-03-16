#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 08:09:34 2024

@author: cornelius
"""


# ----------------------------------- LDOTS ------------------------------------------
"""
                        Lamport Diffie One Time Signature 
                    
                1. Turn a message string into a sequence of k bits
                2. Create a key with k columns and 2*k rows consisting
                   of random 0s and 1s (k is the security parameter)
                3. Create a Verification Key by hashing every element
                   of the key
                4. Create a signature for the message with the key. Every bit
                   of the message gets signed seperately. For every bit of the
                   message the column ( 2 * column_index + bit ) becomes part
                   of the signature.
                5. Verify the signature of the message with the help of the
                   Verification Key. The corresponding columns have to match
                   the hashes of the columns of the signature.
            

"""



# ------------------------------------ IMPORTS --------------------------------

import numpy as np
import hashlib



# --------------------------------- KEY GENERATION ---------------------------






def signing_key(message):
    message = str(message)
    message =  ''.join(format(ord(i), '08b') for i in message)    
    message = [int(i) for i in message]  
    k = len(message) # Security Parameter
    return np.random.randint(0,2,size=(2*k,k)).tolist()


def verification_key(key):
    
    verification_key = []
    
    for c in key:
        column = []
        for r in c:
            column.append(hashlib.sha256(str(r).encode()).hexdigest())
        
        verification_key.append(column)
        
    return verification_key





# ------------------------------- SIGNATURE ----------------------------------


def signature(message,key):
    
    message = str(message)
    message =  ''.join(format(ord(i), '08b') for i in message)    
    message = [int(i) for i in message] 
    
    signature = []
    for idx, bit in enumerate(message):
        signature.append(key[2*idx+bit])
    
    return signature
    
  



# ----------------------------- VERIFICATION ---------------------------------

"""

1. The Recipient receives (Message, Verfication Key, Signature, hash-function)
2. Recipient hashes each element of the Signature
3. Hashed Elements of the Signature get compared with the corresponding
    hashes in the Verification Key using the Message Bits as Reference

"""


def verification(message,verification_key,signature):
    
    message = str(message)
    message =  ''.join(format(ord(i), '08b') for i in message)    
    message = [int(i) for i in message] 
    
    hashed_signature = []
    
    if len(verification_key[0]) != len(message):
        return False
    
    else:
        for c in signature:
            column = []
            for r in c:
                column.append(hashlib.sha256(str(r).encode()).hexdigest())
        
            hashed_signature.append(column)

    
        for idx, bit in enumerate(message):
        
            if verification_key[2*idx+bit] != hashed_signature[idx]:
                return False
        
        return True
        
 




























