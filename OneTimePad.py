from operator import xor
import random


def generate_key_stream(n):
    return bytes([random.randrange(0, 256) for i in range(n)])


def xor_bytes(key_stream, message):
    length = min(len(key_stream), len(message))
    return bytes([key_stream[i] ^ message[i] for i in range(length)])


# this is done by your enemy
message = "YOU ARE AWESOME"
message = message.encode()
key_stream = generate_key_stream(len(message))
cipher = xor_bytes(key_stream, message)
print(key_stream)
print(cipher)
print(xor_bytes(key_stream, cipher))


# this is us trying to break it


# this is us trying to break it
message = "NO ATTACK"
message = message.encode()
guess_key_stream = xor_bytes(message, cipher)
message = xor_bytes(guess_key_stream, cipher)
print(message)


message = "DO ATTACK"
message = message.encode()
guess_key_stream = xor_bytes(message, cipher)
message = xor_bytes(guess_key_stream, cipher)
print(message)
