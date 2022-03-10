
import operator
import sys

# Random text got from google, encrypted using substitution cipher
# Let's try to decrypt it :)
cipher = """el ao xepo dmboc, bxo jdjbjev hoysibebjmd (jh) xehhodl mdvf mdqo edc jb xehhodl
nowmyo bxo wjylb ymidc. jb littolbl xma bxo byedlhmljbjmd jd jh lxmivc hymqooc, el lxmad jd bxo wjtiyo.
wmy oreshvo, jb lefl bxeb bxo jh yohveqol bxo wjylb njb mw bxo myjtjdev hvejd borb nvmqu ajbx bxo wjwbf ojtxbx njb mw bxo myjtjdev hvejd borb,
bxo loqmdc njb ajbx bxo wjwbx njb mw bxo myjtjdev hvejd borb nvmqu, edc lm md. bxjl jl dmbxjdt nib kittvoyf mw njb hmljbjmdl mw bxo myjtjdev hvejd borb nvmqu.
bxo leso yivo ehhvjol bm evv bxo mbxoy njb hmljbjmdl lxmad jd bxo wjtiyo. """


class Attack:
    def __init__(self) -> None:
        self.alphabet = "abcdefghijklmnopqrstuvwxyz"
        self.plain_chars_left = "abcdefghijklmnopqrstuvwxyz"
        self.cipher_chars_left = "abcdefghijklmnopqrstuvwxyz"
        self.freq = {}
        self.key = {}
        self.mappings = {}
        self.freq_eng = {'e': 12.0,
                         't': 9.10,
                         'a': 8.12,
                         'o': 7.68,
                         'i': 7.31,
                         'n': 6.95,
                         's': 6.28,
                         'r': 6.02,
                         'h': 5.92,
                         'd': 4.32,
                         'l': 3.98,
                         'u': 2.88,
                         'c': 2.71,
                         'm': 2.61,
                         'f': 2.30,
                         'y': 2.11,
                         'w': 2.09,
                         'g': 2.03,
                         'p': 1.82,
                         'b': 1.49,
                         'v': 1.11,
                         'k': 0.69,
                         'x': 0.17,
                         'q': 0.11,
                         'j': 0.10,
                         'z': 0.07}
        for f in self.freq_eng:
            self.freq_eng[f] = round(self.freq_eng[f] / 100, 4)

    def calculate_freq(self, cipher):
        for c in self.alphabet:
            self.freq[c] = 0

        letter_count = 0
        for c in cipher:
            if c in self.freq:
                self.freq[c] += 1
                letter_count += 1

        for c in self.freq:
            self.freq[c] = round(self.freq[c] / letter_count, 4)

    def print_freq(self):
        new_line_count = 0
        for c in self.freq:
            print(c, ':', self.freq[c], ' ', end='')
            if new_line_count % 3 == 2:
                print()
            new_line_count += 1

    def calculate_matches(self):
        for cipher_char in self.alphabet:
            map = {}
            for plain_char in self.alphabet:
                map[plain_char] = round(
                    abs(self.freq[cipher_char] - self.freq_eng[plain_char]), 4)
            self.mappings[cipher_char] = sorted(
                map.items(), key=operator.itemgetter(1))

    def set_key_mapping(self, cipher_char, plain_char):
        if cipher_char not in self.cipher_chars_left or plain_char not in self.plain_chars_left:
            print("ERROR: key mapping error", cipher_char, plain_char)
            sys.exit(-1)
        self.key[cipher_char] = plain_char
        self.plain_chars_left = self.plain_chars_left.replace(plain_char, '')
        self.cipher_chars_left = self.cipher_chars_left.replace(
            cipher_char, '')

    def guess_key(self):
        for cipher_char in self.cipher_chars_left:
            for plain_char, diff in self.mappings[cipher_char]:
                if plain_char in self.plain_chars_left:
                    self.key[cipher_char] = plain_char
                    self.plain_chars_left = self.plain_chars_left.replace(
                        plain_char, '')
                    break

    def get_key(self):
        return self.key


def decrypt(key, cipher):
    message = ""
    for c in cipher:
        if c in key:
            message += key[c]
        else:
            message += c
    return message


attack = Attack()
attack.calculate_freq(cipher)
attack.print_freq()
attack.calculate_matches()

attack.set_key_mapping('a', 'w')
attack.set_key_mapping('b', 't')
attack.set_key_mapping('c', 'd')
attack.set_key_mapping('d', 'n')
attack.set_key_mapping('e', 'a')
attack.set_key_mapping('f', 'y')
attack.set_key_mapping('h', 'p')
attack.set_key_mapping('i', 'u')
attack.set_key_mapping('j', 'i')
attack.set_key_mapping('l', 's')
attack.set_key_mapping('m', 'o')
attack.set_key_mapping('n', 'b')
attack.set_key_mapping('o', 'e')
attack.set_key_mapping('p', 'v')
attack.set_key_mapping('q', 'c')
attack.set_key_mapping('r', 'x')
attack.set_key_mapping('s', 'm')
attack.set_key_mapping('t', 'g')
attack.set_key_mapping('u', 'k')
attack.set_key_mapping('w', 'f')
attack.set_key_mapping('x', 'h')
attack.set_key_mapping('y', 'r')

attack.guess_key()
key = attack.get_key()
print()
print(key)
message = decrypt(key, cipher)
message_lines = message.splitlines()
cipher_lines = cipher.splitlines()
print()

for i in range(len(message_lines)):
    print('C:', cipher_lines[i])
    print('P:', message_lines[i])
