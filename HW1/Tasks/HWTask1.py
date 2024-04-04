import hashlib
import itertools

def Bruteforce():
    # Initialize characters with all the possible characters inside the password 
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
 
   # Generate all possible combinations of characters with the specified length
    for password_attempt in itertools.product(characters, repeat=14):
        password_attempt = ''.join(password_attempt)
        check(password_attempt)


def check(string):
    # Change the hash value for different tasks
    target_hash = "94d9e03c11395841301a7aee967864ec"  # Example MD5 hash, replace with the actual target hash

    guessed_pwd = hashlib.md5(string.encode())
    if guessed_pwd.hexdigest() == target_hash:
        print("You succeed and password is", string)
        exit()


Bruteforce()