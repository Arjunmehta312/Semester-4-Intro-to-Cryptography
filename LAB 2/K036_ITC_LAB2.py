#!/usr/bin/env python
# coding: utf-8

# # INTRODUCTION TO CRYPTOGRAPHY LAB 1

# ## Arjun Mehta
# ## K036
# ## B. Tech CSE(Cybersecurity)

# In[12]:


#Encryption

plaintext=input("Enter plain text: ")
keyword=input("Enter key: ")

key=(keyword*(len(plaintext)//len(keyword)))+keyword[:len(plaintext) % len(keyword)]

ciphertext=""

for i in range(len(plaintext)):
    p=plaintext[i]
    if p==' ':
        ciphertext+=' '
    else:
        k=key[i]
        p_val=ord(p.upper())-ord('A')
        k_val=ord(k.upper())-ord('A')
        encrypted_val=(p_val+k_val) % 26
        encrypted_char=chr(encrypted_val+ord('A'))
        ciphertext+=encrypted_char

print(f"Ciphertext is: {ciphertext}")


# In[13]:


#Decryption

ciphertext=input("Enter cipher to be decrypted: ")
keyword=input("Enter key: ")

key=(keyword*(len(ciphertext)//len(keyword)))+keyword[:len(ciphertext)%len(keyword)]

plaintext=""

for i in range(len(ciphertext)):
    c=ciphertext[i]
    if c==' ':
        plaintext+=' '
    else:
        k=key[i]
        c_val=ord(c.upper())-ord('A')
        k_val=ord(k.upper())-ord('A')
        decrypted_val=(c_val-k_val+26)%26
        decrypted_char=chr(decrypted_val+ord('A'))
        plaintext+=decrypted_char

print(f"Decrypted Text: {plaintext}")

