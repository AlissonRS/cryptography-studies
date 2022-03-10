import random

# This uses a pseudo-random function, just for learning purposes
# meaning this is not secure for a real-world use case :)


def generate_key():
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".lower()
    cletters = list(letters)
    key = {}
    for c in letters:
        key[c] = cletters.pop(random.randint(0, len(cletters) - 1))
    return key


def encrypt(key, message):
    cipher = ""
    for c in message:
        if c in key:
            cipher += key[c]
        else:
            cipher += c
    return cipher


def get_decrypt_key(key):
    dkey = {}
    for k in key:
        dkey[key[k]] = k
    return dkey


key = generate_key()
print(key)
message = """as we have noted, the initial permutation (ip) happens only once and it happens before the first round. it suggests how the transposition in ip should proceed, as shown in the figure. for example, it says that the IP replaces the first bit of the original plain text block with the fifty eighth bit of the original plain text, the second bit with the fifth bit of the original plain text block, and so on. This is nothing but jugglery of bit positions of the original plain text block. the same rule applies to all the other bit positions shown in the figure."""
cipher = encrypt(key, message.lower())
print(cipher)
dkey = get_decrypt_key(key)
message = encrypt(dkey, cipher)
print(message)
