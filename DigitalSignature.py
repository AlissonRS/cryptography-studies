# These are Alice's RSA keys
# Public key (e,n): 5 170171
# Secret key (d): 9677

import hashlib


n = 170171
e = 5
d = 9677


def modify(m):
    l = list(m)
    l[0] = l[0] ^ 1
    return bytes(l)


# This is the message that Alice wants to sign and send to Bob
message = "Bob you are awesome".encode()

# Step 1: hash the message
sha256 = hashlib.sha256()
sha256.update(message)
h = sha256.digest()
# the module here is typically not done in real world
h = int.from_bytes(h, "big") % n
print("Hash value", h)


# Step 2: decrypt the hash value (use secret exponent)
sign = h**d % n

# Step 3: send message with signature to Bob
print(message, sign)


# This is Eve being evil and modifies the message
message = modify(message)
print(message)

# Bob verifying the signature

# Step 1: calculate the hash value of the message
sha256 = hashlib.sha256()
sha256.update(message)
h = sha256.digest()
h = int.from_bytes(h, "big") % n
print("Hash value", h)

# Step 2: Verify the signature
verification = sign ** e % n
print("Verification value", verification)
