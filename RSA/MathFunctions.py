#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 12:02:23 2025

@author: cornelius
"""


#Euklid Algorithm to calculate the greatest common divisor 
#Used to calcualte the public key
def GCD(a,b):
    a_list = []
    b_list = []
    rest = 1
    a_list.append(a)
    b_list.append(b)
    q_list = []
    
    while rest != 0:
        rest = a%b
        q = (a-rest)/b
        q_list.append(q)
        a = b
        b = rest
        a_list.append(a)
        b_list.append(b)
    
    ggT = b_list[len(b_list)-2]
    return ggT


#Advanced Euklid Algorithm to calculate the multipicative Inverse of the public key
#Used to calcualte the private key
def multiplicativeInverse(a,b):

    a_list = []
    b_list = []
    rest = 1
    a_list.append(a)
    b_list.append(b)
    q_list = []
    
    while rest != 0:
        rest = a%b
        q = (a-rest)/b
        q_list.append(q)
        a = b
        b = rest
        a_list.append(a)
        b_list.append(b)
    
    
    x = 0
    y = 1
    
    x_list = []
    y_list = []
    x_list.append(x)
    y_list.append(y)
    
    rev_q_list = list(reversed(q_list))

    
    for i in range(1,len(a_list)-1):
        x = y_list[i-1]
        x_list.append(x)
        y = x_list[i-1] - rev_q_list[i]*y_list[i-1]
        y_list.append(y)
        pass
    
    inverse = x_list[len(x_list)-1]%b_list[0]
    
    return inverse


# easy implementation of modular exponent
def modular_exponent(a,b,n):
    result = 1
    for i in range(0,b):
        result *= a
        result %= n
    
    return result


# fast implementation of modular exponent
def fastModularExponent(a,b,n):
    binary_list = []
    binary_string = str(bin(b))
    for i in range(2,len(binary_string)):
        binary_list.append(binary_string[i])

    binary_list.reverse()
    
    #print(binary_list)
    
    # calculate squares
    square_list = []
    square = a
    square_list.append(a)
    for i in range(0,len(binary_list)-1):
        square = (square**2)%n
        square_list.append(square)
    
    #print(square_list)
    
    # Multiply the squares
    product = 1
    binary_squares = list(zip(binary_list,square_list))
    #print(binary_squares)
    
    for element in binary_squares:
        if element[0]=='1':
            product *= element[1]%n
    
    return product%n


