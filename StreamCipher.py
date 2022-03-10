import random
import string


class KeyStream:
    def __init__(self, key=1) -> None:
        self.next = key

    def rand(self):
        self.next = (1103515245 * self.next + 12345) % 2**31
        return self.next

    def get_key_byte(self):
        return (self.rand()//2**23) % 256


def encrypt(key, message):
    return bytes([message[i] ^ key.get_key_byte() for i in range(len(message))])


def transmit(cipher, likely):
    b = []
    for c in cipher:
        if random.randrange(0, likely) == 0:
            c = c ^ 2**random.randrange(0, 8)
        b.append(c)
    return bytes(b)


def modification(cipher):
    mask = [0]*len(cipher)
    mask[10] = ord(' ') ^ ord('1')
    mask[11] = ord(' ') ^ ord('0')
    mask[12] = ord('1') ^ ord('0')
    return bytes([mask[i] ^ cipher[i] for i in range(len(cipher))])


def shift_nth_byte(cipher, nth_byte, nth_bit):
    b = []
    i = 0
    for c in cipher:
        if (i == nth_byte):
            c = c ^ 1 << (nth_bit)
        b.append(c)
        i += 1
    return bytes(b)


def get_key(message, cipher):
    return bytes([message[i] ^ cipher[i] for i in range(len(cipher))])


def crack(key_stream, cipher):
    length = min(len(key_stream), len(cipher))
    return bytes([key_stream[i] ^ cipher[i] for i in range(length)])


def brute_force(plain, cipher):
    for k in range(2**31):
        bf_key = KeyStream(k)
        for i in range(len(plain)):
            xor_value = plain[i] ^ cipher[i]
            if xor_value != bf_key.get_key_byte():
                break
        else:
            return k
    return False


def test_transmit():
    key = KeyStream(10)
    message = "Hello, World! I am here to declare that I will take over the universe and become the supreme emperor".encode()
    print("Original Message: ", message)
    cipher = encrypt(key, message)
    print(cipher)
    cipher = transmit(cipher, 5)

    key = KeyStream(10)
    message = encrypt(key, cipher)
    print("Hacked Message: ", message)


def test_shift_nth_bit():
    key = KeyStream(10)
    message = "Hello, World! I am here to declare that I will take over the universe and become the supreme emperor".encode()
    print("Original Message: ", message)
    cipher = encrypt(key, message)
    print(cipher)
    cipher = shift_nth_byte(cipher, 3, 5)

    key = KeyStream(10)
    message = encrypt(key, cipher)
    print("Hacked Message: ", message)


def test_modification():
    key = KeyStream(10)
    message = "Send Bob:   10$".encode()
    print("Original Message: ", message)
    cipher = encrypt(key, message)
    print(cipher)
    cipher = modification(cipher)

    key = KeyStream(10)
    message = encrypt(key, cipher)
    print("Hacked Message: ", message)


def test_crack_stream_key():
    # Eve goes to Alice
    eves_message = "This is Eve's most valued secrets of all her life.".encode()

    # This is Alice alone
    key = KeyStream(10)
    message = eves_message
    print("Eve's Message: ", message)
    cipher = encrypt(key, message)
    print(cipher)

    # This is Eve (alone) all evil
    eves_key_stream = get_key(eves_message, cipher)

    # This is Bob
    key = KeyStream(10)
    message = encrypt(key, message)
    print(message)

    # Alice again
    message = "Hi Bob, let's meet a plan our world domination.".encode()
    key = KeyStream(10)
    cipher = encrypt(key, message)
    print(cipher)

    # Bob again
    key = KeyStream(10)
    message = encrypt(key, message)
    print(message)

    # Eve again (more evil than ever)
    print("THIS IS EVE")
    print(crack(eves_key_stream, cipher))


# This is Alice
secret_key = random.randrange(0, 2**25)
print(secret_key)
key = KeyStream(secret_key)
header = "MESSAGE: "
message = header + "My secret message to Bob"
message = message.encode()
print(message)
cipher = encrypt(key, message)
print(cipher)

# This is Bob
key = KeyStream(secret_key)
message = encrypt(key, cipher)
print(message)

# This is Eve
bf_key = brute_force(header.encode(), cipher)
print("Eve's brute force key:", bf_key)
key = KeyStream(bf_key)
message = encrypt(key, cipher)
print(message)
