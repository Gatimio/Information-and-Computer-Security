import hashlib
import itertools

def Bruteforce():
    # Write your code here
    char_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    char_lower = "abcdefghijklmnopqrstuvwxyz"
    char_dig = "0123456789"


    for u1 in char_upper:
        for u2 in char_upper:
            for u3 in char_upper:
                for u4 in char_upper:
                    for d1 in char_dig:
                        for d2 in char_dig:
                            for d3 in char_dig:
                                for l1 in char_lower:
                                    for l2 in char_lower:
                                        for l3 in char_lower:
                                            for l4 in char_lower:
                                                pass_attempt = u1 + u2 + u3 + u4 + d1 + d2 + d3 + l1 + l2 + l3 + l4 

                                                check(pass_attempt)

def check(string):
    # Change the hash value for different tasks
    target_hash = "f593def02f37f3a6d57bcbc9480a3316"  # Example MD5 hash, replace with the actual target hash

    guessed_pwd = hashlib.md5(string.encode())
    if guessed_pwd.hexdigest() == target_hash:
        print("You succeed and password is", string)
        exit()

Bruteforce()