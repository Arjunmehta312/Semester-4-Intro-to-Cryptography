#!/usr/bin/env python
# coding: utf-8

# ## INTRODUCTION TO CRYPTOGRAPHY LAB 5
# ## Arjun Mehta
# ## K036
# ## B. Tech CSE(Cybersecurity)

# In[6]:


# Diffie-Hellman Key Exchange Implementation with user input and detailed output

def mod_exp(base, exp, mod):
    if exp == 0:
        return 1
    half_exp = mod_exp(base, exp // 2, mod)
    half_exp = (half_exp * half_exp) % mod
    if exp % 2 != 0:
        half_exp = (half_exp * base) % mod
    return half_exp

def is_primitive_root(g, p):
    required_set = set(num for num in range(1, p) if gcd(num, p) == 1)
    actual_set = set(mod_exp(g, powers, p) for powers in range(1, p))
    return required_set == actual_set

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

p = int(input("Enter a prime number p: "))
g = int(input("Enter a base g (primitive root of p): "))

if not is_primitive_root(g, p):
    print(f"{g} is not a primitive root of {p}. Please choose another base.")
    exit()

a = 6
A = mod_exp(g, a, p)
print(f"Alice sends A = {A} to Bob")

b = 15
B = mod_exp(g, b, p)
print(f"Bob sends B = {B} to Alice")

shared_secret_Alice = mod_exp(B, a, p)
print(f"Alice computes the shared secret: {shared_secret_Alice}")

shared_secret_Bob = mod_exp(A, b, p)
print(f"Bob computes the shared secret: {shared_secret_Bob}")

assert shared_secret_Alice == shared_secret_Bob, "Shared secrets do not match!"
print("Shared secret key exchange successful!")

output_list = []
elements = [2, 4, 3, 1]

for element in elements:
    output_list.append(element)
    print(output_list)

