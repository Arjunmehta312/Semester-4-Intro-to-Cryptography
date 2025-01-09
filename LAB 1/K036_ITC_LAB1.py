#!/usr/bin/env python
# coding: utf-8

# # INTRODUCTION TO CRYPTOGRAPHY LAB 1

# ## Arjun Mehta
# ## K036
# ## B. Tech CSE(Cybersecurity)

# In[1]:


#Encryption

ptext = input("Enter plain text: ")
key = int(input("Enter Key: "))
ptext = list(ptext)

for i in range(len(ptext)):
    ch = ptext[i]
    
    if 'a' <= ch <= 'z':
        ch = chr(((ord(ch) - ord('a') + key) % 26) + ord('a'))
        ptext[i] = ch
    elif 'A' <= ch <= 'Z':
        ch = chr(((ord(ch) - ord('A') + key) % 26) + ord('A'))
        ptext[i] = ch

encrypted_text = ''.join(ptext)
print("Encrypted text is:", encrypted_text)


# In[2]:


#Decryption

ctext = input("Enter cipher text: ")
key = int(input("Enter Key: "))
ctext = list(ctext)

for i in range(len(ctext)):
    ch = ctext[i]
    
    if 'a' <= ch <= 'z':
        ch = chr(((ord(ch) - ord('a') - key) % 26) + ord('a'))
        ctext[i] = ch
    elif 'A' <= ch <= 'Z':
        ch = chr(((ord(ch) - ord('A') - key) % 26) + ord('A'))
        ctext[i] = ch

decrypted_text = ''.join(ctext)
print("Decrypted text is:", decrypted_text)


# In[3]:


#Brute Force

ctext = input("Enter cipher text: ")
ctext = list(ctext)

for key in range(26):
    for i in range(len(ctext)):
        ch = ctext[i]
        
        if 'a' <= ch <= 'z':
            ch = chr(((ord(ch) - ord('a') - (key+1)) % 26) + ord('a'))
            ctext[i] = ch
        elif 'A' <= ch <= 'Z':
            ch = chr(((ord(ch) - ord('A') - (key+1)) % 26) + ord('A'))
            ctext[i] = ch
    
    decrypted_text = ''.join(ctext)
    print(f"Decrypted text for key={key+1} is: {decrypted_text}")


# In[ ]:




