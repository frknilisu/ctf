#! /usr/bin/env python3
##
# Solution for RSA256 challenge
# by Amos Ng
##
# Imports
from Crypto.PublicKey import RSA
import math

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def factorise(n):
    x = math.ceil(math.sqrt(n))
    y = x**2 - n
    while not math.sqrt(y).is_integer():
        x += 1
        y = x**2 - n
    return x + math.sqrt(y), x - math.sqrt(y)

def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

# Import public key
pubkey = RSA.importKey(open('public.key', 'r').read())

# Define initial variables
n = pubkey.n
e = pubkey.e

# Use factordb
p = 277271726050281009396301232126405463677
q = 224258454597761606450883324956139951511

# Calculate private d
phi = (p-1) * (q-1)
d = modinv(e, phi)

privkey = RSA.construct((n, e, d, p, q))
privpem = privkey.exportKey('PEM').decode()
print("Flag: %s" % privpem.split("\n")[1][:32])
