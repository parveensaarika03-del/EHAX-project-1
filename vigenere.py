def encrypt(text, key):
    result = ""
    key = key.upper()
    j = 0

    for ch in text:
        if ch.isalpha():
            shift = ord(key[j % len(key)]) - 65

            if ch.isupper():
                result += chr((ord(ch) - 65 + shift) % 26 + 65)
            else:
                result += chr((ord(ch) - 97 + shift) % 26 + 97)

            j += 1
        else:
            result += ch

    return result


def decrypt(text, key):
    result = ""
    key = key.upper()
    j = 0

    for ch in text:
        if ch.isalpha():
            shift = ord(key[j % len(key)]) - 65

            if ch.isupper():
                result += chr((ord(ch) - 65 - shift) % 26 + 65)
            else:
                result += chr((ord(ch) - 97 - shift) % 26 + 97)

            j += 1
        else:
            result += ch

    return result






choice = input("Enter E for Encrypt or D for Decrypt: ").upper()
choice = choice.strip()

if choice == "E":

    mode = input("Enter T for Text or F for File: ").upper()

    key = input("Enter key: ")

    if mode == "T":

        text = input("Enter message: ")

        encrypted = encrypt(text, key)

        print("\nEncrypted text:")
        print(encrypted)

    elif mode == "F":

        filename = input("Enter file relaive path: ")

        file = open(filename, "r")
        text = file.read()
        file.close()

        encrypted = encrypt(text, key)

        output = open("encrypted.txt", "w")
        output.write(encrypted)
        output.close()

        print("\nEncrypted data saved in encrypted.txt")

    else:
        print("Invalid choice")


elif choice == "D":

    mode = input("Enter T for Text or F for File: ").upper()

    key = input("Enter key: ")

    if mode == "T":

        text = input("Enter encrypted message: ")

        decrypted = decrypt(text, key)

        print("\nDecrypted text:")
        print(decrypted)

    elif mode == "F":

        filename = input("Enter file relative: ")

        file = open(filename, "r")
        text = file.read()
        file.close()

        decrypted = decrypt(text, key)

        output = open("decrypted.txt", "w")
        output.write(decrypted)
        output.close()

        print("\nDecrypted data saved in decrypted.txt")

    else:
        print("Invalid choice")


else:
    print("Please enter E or D.")
