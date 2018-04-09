# vigenere cipher

import random
alphabet = " !\"#$%&'-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}`"
users = ["gkim3783", "lara_chunko"]
salt =["Q6gao]lF0}?RPxHP", "=hDT!}g C288]|JPK4%U2j5{"] 
hash_list = ["x{z}6MQd9]@u5G6@N<(M&(Q{X", "xg ne}F~S`1+i3E2<As,V`X68W2n>2"]  

def salting():
    n = 0
    salt = ""
    while n < (30 - len(originaltext)):
        random_character = random.choice(alphabet)
        salt += random_character
        n += 1
    return salt

def find_salt(key):
    for name in users:
        if name == keyword:
            nth_term = int(users.index(key))
    salt_string = salt[nth_term]
    return salt_string 

def encrypt(plaintext, key):
    key_number = [ord(i) for i in key]
    plaintext_number = [ord(i) for i in plaintext]
    ciphertext = ""
    for i in range(len(plaintext_number)):
        value = (plaintext_number[i] - 32 + key_number[i % len(key)])% 95
        ciphertext += chr(value + 32)
    return ciphertext

def decrypt(ciphertext, key):
    key_number = [ord(i) for i in key]
    ciphertext_number = [ord(i) for i in ciphertext]
    plaintext = ""
    for i in range(len(ciphertext_number)):
        value = (ciphertext_number[i] - 32 - key_number[i % len(key)])% 95
        plaintext += chr(value + 32)
    return plaintext

def hashinginput(originaltext):
    if len(originaltext) > 30:
        print("Password can be 30 characters maximum.")
        newtext = ""
    else:
        newtext = originaltext + find_salt(keyword) 
    return newtext

def get_correct_hash(key): 
    for name in users:
        if name == keyword:
            nth_term = int(users.index(key))
    correct_hash = hash_list[nth_term]
    return correct_hash


variable = str(input("new user or login or pass: "))
if variable == "login":
    keyword = str(input("username = "))
    originaltext = str(input("password = "))
    combinedtext = hashinginput(originaltext)
    hash = encrypt(combinedtext, keyword)
    correct_hash = get_correct_hash(keyword)
    if hash == correct_hash:
        print("Welcome, " + keyword)
    if hash != correct_hash:
        print("Login information is wrong. Please try again.")

elif variable == "new user":
    keyword = str(input("enter your new username: "))
    for name in users:
        if name == keyword:
            print("This username has already been taken.")
            raise SystemExit() #https://community.activestate.com/forum/using-python-how-do-i-terminate-stop-execution-my-script
        else:
            users.append(keyword) 
            new_salt = str(salt)
            salt.append(new_salt) 
            originaltext = str(input("enter your new password: "))
            combinedtext = originaltext + new_salt
            new_hash = str(encrypt(combinedtext, keyword))
            hash_list.append(new_hash)
            print(users)
            print(salt)
            print(hash_list) 
    
elif variable == "pass":
    print(users)
    print(salt)
    print(hash_list) 

      
