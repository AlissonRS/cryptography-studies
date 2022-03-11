import hashlib
import base64


def guess_password(salt, iterations, entropy):
    alphabet = '?abcdefghijklmnopqrstuvwxyz'
    for c1 in alphabet:
        for c2 in alphabet:
            password = str.encode(c1 + c2)
            value = base64.b64encode(hashlib.pbkdf2_hmac(
                "sha512", password, salt, iterations, dklen=128))
            if value == entropy:
                return password
    return "".encode()


iterations = 45454
salt = base64.b64decode(
    "6VuJKkHVTdDelbNMPBxzw7INW2NkYlR/LoW40L7kVAI=".encode())
validation = "SALTED-SHA12-PBKDF2"
entropy = "qoUHPDbnXS3iGIyhysUyr0WRSfva6tACvbLtt1F4uXHStP911ZmLFoYRkYlZDv6PVlnsqISTsWP63h57+0hQM8IuIU8JAy4U6UjRAszNTRSDJc/OB55iLj/cVQcynSbNUOPV/4E4b9jzvSLA+D3lMfIkds+KiaGb+hdwH91JWtE="

password = "??".encode()

password = guess_password(salt, iterations, entropy)
print(password)
value = base64.b64encode(hashlib.pbkdf2_hmac(
    "sha512", password, salt, iterations, dklen=128))
print(value)
print(entropy)
