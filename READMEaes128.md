**AES-128 (ADVANCED ENCRYPTION STANDARD)-128**

A SMALL OVERVIEW:
AES-128 takes the message and first mixes it with the encryption key. Then it performs 10 rounds of scrambling. In each of the first 9 rounds, it does four things: SubBytes replaces each byte with another value, ShiftRows rearranges the bytes, MixColumns mixes the bytes together, and AddRoundKey combines them with a different round key. The 10th round does the same thing except it skips MixColumns. After all 10 rounds, the result is the encrypted/ciphertext. During decryption, these steps are performed in reverse to get the original message back.
(this is only a summary, because the whole process in detailed is complicated to explain in text)

DESCRIPTION:
its a simple AES-128 based encryption/decryption python program where you input text or a txt file path address and it gives you encrypted/decrypted text string/ file according to your selection.

FEATURES:
It askes the user weather to encrypt or decrypt the message
It asks the user for the "16-character key" upon which the whole cryptography works.MAKE SURE YOU ENTER A 16-CHARACTER KEY ONLY.
it works on both text strings input by the user and txt files pre existing in user's system.

USAGE:
you can run the python file in either python interpreter or in terminal by using python vigenere.py or python3 vigenere.py 
upon hitting 'run', the program will ask you weather you want to encrypt or decrypt your message, for encrypting press 'e', for decrypting press 'd', then it'll ask u weather if you wanna use txt fil for or input text string for the cryptography, enter 'f' for file and 't' if you want to input text string.
it will now ask you for 16 character key, enter the key.
enter text string/ enter relative file path address
your encrypted/decrypted text will be displayed or your encrypted/decrypted file will be saved as "encrypted.txt" or "decrypted.txt" respectively in /Documents/
