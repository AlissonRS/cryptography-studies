def generate_key(n):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key = {}
    cnt = 0
    for c in letters:
        key[c] = letters[(cnt + n) % len(letters)]
        cnt += 1
    return key


def encrypt(key, message):
    cipher = ""
    for c in message:
        if c in key:
            cipher += key[c]
        else:
            cipher += c
    return cipher


def get_decryption_key(key):
    dkey = {}
    for c in key:
        dkey[key[c]] = c
    return dkey


key = generate_key(3)
cipher = encrypt(key, "YOU ARE AWESOME")
print(cipher)
dkey = get_decryption_key(key)
message = encrypt(dkey, cipher)
print(message)
