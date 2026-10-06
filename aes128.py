SBOX = [
99,124,119,123,242,107,111,197,48,1,103,43,254,215,171,118,
202,130,201,125,250,89,71,240,173,212,162,175,156,164,114,192,
183,253,147,38,54,63,247,204,52,165,229,241,113,216,49,21,
4,199,35,195,24,150,5,154,7,18,128,226,235,39,178,117,
9,131,44,26,27,110,90,160,82,59,214,179,41,227,47,132,
83,209,0,237,32,252,177,91,106,203,190,57,74,76,88,207,
208,239,170,251,67,77,51,133,69,249,2,127,80,60,159,168,
81,163,64,143,146,157,56,245,188,182,218,33,16,255,243,210,
205,12,19,236,95,151,68,23,196,167,126,61,100,93,25,115,
96,129,79,220,34,42,144,136,70,238,184,20,222,94,11,219,
224,50,58,10,73,6,36,92,194,211,172,98,145,149,228,121,
231,200,55,109,141,213,78,169,108,86,244,234,101,122,174,8,
186,120,37,46,28,166,180,198,232,221,116,31,75,189,139,138,
112,62,181,102,72,3,246,14,97,53,87,185,134,193,29,158,
225,248,152,17,105,217,142,148,155,30,135,233,206,85,40,223,
140,161,137,13,191,230,66,104,65,153,45,15,176,84,187,22
]

INV_SBOX = [0] * 256

for i in range(256):
    INV_SBOX[SBOX[i]] = i


RCON = [0,1,2,4,8,16,32,64,128,27,54]


def multiply(a, b):

    result = 0

    for i in range(8):

        if b & 1:
            result = result ^ a

        if a & 128:
            a = ((a << 1) ^ 27) & 255
        else:
            a = (a << 1) & 255

        b = b >> 1

    return result


def make_keys(key):

    words = []

    for i in range(4):

        words.append([
            key[i * 4],
            key[i * 4 + 1],
            key[i * 4 + 2],
            key[i * 4 + 3]
        ])

    for i in range(4, 44):

        temp = words[i - 1][:]

        if i % 4 == 0:

            temp = temp[1:] + temp[:1]

            for j in range(4):
                temp[j] = SBOX[temp[j]]

            temp[0] = temp[0] ^ RCON[i // 4]

        word = []

        for j in range(4):
            word.append(words[i - 4][j] ^ temp[j])

        words.append(word)

    keys = []

    for r in range(11):

        key = []

        for i in range(4):
            key += words[r * 4 + i]

        keys.append(key)

    return keys


def add_key(state, key):

    for i in range(16):
        state[i] ^= key[i]


def sub_bytes(state):

    for i in range(16):
        state[i] = SBOX[state[i]]


def inverse_sub_bytes(state):

    for i in range(16):
        state[i] = INV_SBOX[state[i]]


def shift_rows(state):

    old = state[:]

    state[0] = old[0]
    state[1] = old[5]
    state[2] = old[10]
    state[3] = old[15]

    state[4] = old[4]
    state[5] = old[9]
    state[6] = old[14]
    state[7] = old[3]

    state[8] = old[8]
    state[9] = old[13]
    state[10] = old[2]
    state[11] = old[7]

    state[12] = old[12]
    state[13] = old[1]
    state[14] = old[6]
    state[15] = old[11]


def inverse_shift_rows(state):

    old = state[:]

    state[0] = old[0]
    state[1] = old[13]
    state[2] = old[10]
    state[3] = old[7]

    state[4] = old[4]
    state[5] = old[1]
    state[6] = old[14]
    state[7] = old[11]

    state[8] = old[8]
    state[9] = old[5]
    state[10] = old[2]
    state[11] = old[15]

    state[12] = old[12]
    state[13] = old[9]
    state[14] = old[6]
    state[15] = old[3]


def mix_columns(state):

    for i in range(0, 16, 4):

        a = state[i]
        b = state[i + 1]
        c = state[i + 2]
        d = state[i + 3]

        state[i] = (
            multiply(a, 2) ^
            multiply(b, 3) ^
            c ^ d
        )

        state[i + 1] = (
            a ^
            multiply(b, 2) ^
            multiply(c, 3) ^
            d
        )

        state[i + 2] = (
            a ^ b ^
            multiply(c, 2) ^
            multiply(d, 3)
        )

        state[i + 3] = (
            multiply(a, 3) ^
            b ^ c ^
            multiply(d, 2)
        )


def inverse_mix_columns(state):

    for i in range(0, 16, 4):

        a = state[i]
        b = state[i + 1]
        c = state[i + 2]
        d = state[i + 3]

        state[i] = (
            multiply(a, 14) ^
            multiply(b, 11) ^
            multiply(c, 13) ^
            multiply(d, 9)
        )

        state[i + 1] = (
            multiply(a, 9) ^
            multiply(b, 14) ^
            multiply(c, 11) ^
            multiply(d, 13)
        )

        state[i + 2] = (
            multiply(a, 13) ^
            multiply(b, 9) ^
            multiply(c, 14) ^
            multiply(d, 11)
        )

        state[i + 3] = (
            multiply(a, 11) ^
            multiply(b, 13) ^
            multiply(c, 9) ^
            multiply(d, 14)
        )


def encrypt_block(block, keys):

    state = block[:]

    add_key(state, keys[0])

    for r in range(1, 10):

        sub_bytes(state)
        shift_rows(state)
        mix_columns(state)
        add_key(state, keys[r])

    sub_bytes(state)
    shift_rows(state)
    add_key(state, keys[10])

    return state


def decrypt_block(block, keys):

    state = block[:]

    add_key(state, keys[10])

    for r in range(9, 0, -1):

        inverse_shift_rows(state)
        inverse_sub_bytes(state)
        add_key(state, keys[r])
        inverse_mix_columns(state)

    inverse_shift_rows(state)
    inverse_sub_bytes(state)
    add_key(state, keys[0])

    return state


def pad(data):

    amount = 16 - len(data) % 16

    for i in range(amount):
        data.append(amount)

    return data


def remove_padding(data):

    amount = data[-1]

    return data[:-amount]


def text_to_numbers(text):

    result = []

    for ch in text:
        result.append(ord(ch))

    return result


def numbers_to_text(data):

    text = ""

    for n in data:
        text += chr(n)

    return text


def to_hex(data):

    result = ""

    for n in data:
        result += format(n, "02x")

    return result


def from_hex(text):

    result = []

    for i in range(0, len(text), 2):
        result.append(int(text[i:i + 2], 16))

    return result


def encrypt_text(text, key):

    data = text_to_numbers(text)
    data = pad(data)

    keys = make_keys(text_to_numbers(key))

    result = []

    for i in range(0, len(data), 16):

        block = data[i:i + 16]

        encrypted = encrypt_block(block, keys)

        result += encrypted

    return to_hex(result)


def decrypt_text(ciphertext, key):

    data = from_hex(ciphertext)

    keys = make_keys(text_to_numbers(key))

    result = []

    for i in range(0, len(data), 16):

        block = data[i:i + 16]

        decrypted = decrypt_block(block, keys)

        result += decrypted

    result = remove_padding(result)

    return numbers_to_text(result)




choice = input("Enter E for Encrypt or D for Decrypt: ").upper()

mode = input("Enter T for Text or F for File: ").upper()

key = input("Enter 16-character key: ")

if len(key) != 16:

    print("Key must be exactly 16 characters.")

else:

    if choice == "E":

        if mode == "T":

            text = input("Enter message: ")

            encrypted = encrypt_text(text, key)

            print("\nEncrypted text:")
            print(encrypted)

        elif mode == "F":

            filename = input("Enter file name: ")

            file = open(filename, "r")
            text = file.read()
            file.close()

            encrypted = encrypt_text(text, key)

            file = open("encrypted.txt", "w")
            file.write(encrypted)
            file.close()

            print("\nEncrypted file created: encrypted.txt")

        else:

            print("Invalid mode.")

    elif choice == "D":

        if mode == "T":

            ciphertext = input("Enter hexadecimal ciphertext: ")

            try:

                decrypted = decrypt_text(ciphertext, key)

                print("\nDecrypted text:")
                print(decrypted)

            except:

                print("Invalid ciphertext.")

        elif mode == "F":

            filename = input("Enter encrypted file name: ")

            file = open(filename, "r")
            ciphertext = file.read()
            file.close()

            try:

                decrypted = decrypt_text(ciphertext, key)

                file = open("decrypted.txt", "w")
                file.write(decrypted)
                file.close()

                print("\nDecrypted file created: decrypted.txt")

            except:

                print("Invalid encrypted file.")

        else:

            print("Invalid mode.")

    else:

        print("Please enter E or D.")
