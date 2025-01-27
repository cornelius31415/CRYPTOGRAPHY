#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 14:42:28 2025

@author: cornelius
"""


message = "i love you"
key = 12


def encrypt(plaintext,key):
    
    encryptedMessage = [(ord(char) + key) % 128 for char in plaintext]
    return encryptedMessage
        


def decrypt(secret,key):
    
    decryptedMessage = ""
    for number in secret:
        decryptedMessage += chr((number - key) % 128)
    
    return decryptedMessage


secret = encrypt(message,key)
print(secret)
plaintext = decrypt(secret,key)
print(plaintext)
