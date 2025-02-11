#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 14:27:27 2025

@author: cornelius
"""

# -----------------------------------------------------------------------
#                               IMPORTS   
# -----------------------------------------------------------------------

from math import gcd
import time
from BruteForce import factorizeBruteForce
from Pollard_p1 import factorizeP1
from Pollard_rho import factorizeRho

# -----------------------------------------------------------------------
#                               TESTING   
# -----------------------------------------------------------------------


n = 1372319802547       #    = 174440041*7867

n_binary = bin(n)[2:]
bitLength = len(n_binary)

print(f"\nNumber to factorize:   {n}")
print(f"Binary:                {n_binary}")
print(f"Amount of Bits         {bitLength} \n")

print("-----------------------------------------------------------------")
print("                      FACTORIZATION METHODS")
print("-----------------------------------------------------------------")

# -----------------------------------------------------------------------
#                               BRUTE FORCE   
# -----------------------------------------------------------------------

start1 = time.time()

primeFactor = factorizeBruteForce(n)

end1 = time.time()
runtime1 = end1 - start1

print(f"\nBrute Force Factors:               {primeFactor}")
print(f"Brute Force Factorization Runtime:{runtime1: .4f} s \n")



# -----------------------------------------------------------------------
#                               POLLARD p-1   
# -----------------------------------------------------------------------

start2 = time.time()

primeFactor = factorizeP1(n)

end2 = time.time()
runtime2 = end2 - start2

print(f"Pollard p-1 Factors:               {primeFactor}")
print(f"Pollard p-1 Runtime:              {runtime2: .8f} s \n")
    




# -----------------------------------------------------------------------
#                               POLLARD RHO   
# -----------------------------------------------------------------------

start3 = time.time()

primeFactor = factorizeRho(n)

end3 = time.time()
runtime3 = end3 - start3

print(f"Pollard rho Factors:               {primeFactor}")
print(f"Pollard rho Runtime:              {runtime3: .8f}s")





# -----------------------------------------------------------------------
#                               COMPARISON   
# -----------------------------------------------------------------------

print(f"\nPollard's (p-1)-Algorithm is {round(runtime1/runtime2,1)} times faster than the Brute Force Algorithm.")

print(f"\nPollard's rho-Algorithm is {round(runtime2/runtime3,1)} times faster than the Pollard (p-1)-Algorithm.")

print(f"\nPollard's rho-Algorithm is {round(runtime1/runtime3,1)} times faster than the Brute Force Algorithm.")





















