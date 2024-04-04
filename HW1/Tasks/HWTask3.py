import hashlib
import itertools

def Bruteforce():
    # Write your code here
    char_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "1234"
    length = 11

    # Generate all possible combinations
    combinations = itertools.product(char_upper, repeat=7)
    
    for combo in combinations:
        # Insert "1234" at different positions
        for i in range(8):
            current_password = ''.join(combo[:i] + tuple(digits) + combo[i:])
            check(current_password)

def check(string):
    # Change the hash value for different tasks
    target_hash = "bfb2c12706757b8324368de6a365338b"  # Example MD5 hash, replace with the actual target hash

    guessed_pwd = hashlib.md5(string.encode())
    if guessed_pwd.hexdigest() == target_hash:
        print("You succeed and password is", string)

        exit()

Bruteforce()