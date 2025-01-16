#!/usr/bin/env python
# coding: utf-8

# # INTRODUCTION TO CRYPTOGRAPHY LAB 1

# ## Arjun Mehta
# ## K036
# ## B. Tech CSE(Cybersecurity)

# In[17]:


def mod_inverse(a,m):
    for x in range(1,m):
        if (a*x)%m==1:
            return x
    return None

plaintext = input("Enter plaintext: ")
a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))


# In[18]:


def affine_encrypt(plaintext,a,b):
    return ''.join(chr(((a*(ord(char)-ord('A'))+b)%26)+ord('A')) if char.isalpha() else char for char in plaintext.upper())

ciphertext = affine_encrypt(plaintext, a, b)
print(f"Encrypted Text: {ciphertext}")


# In[19]:


def affine_decrypt(ciphertext, a, b):
    a_inv = mod_inverse(a, 26)
    return ''.join(chr((a_inv*((ord(char)-ord('A'))-b)%26)+ord('A')) if char.isalpha() else char for char in ciphertext.upper())

decrypted_text = affine_decrypt(ciphertext, a, b)
print(f"Decrypted Text: {decrypted_text}")


# In[ ]:




