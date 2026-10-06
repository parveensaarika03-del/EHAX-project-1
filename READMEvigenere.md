**VIGENERE CIPHER**

A SMALL OVERVIEW:
Vigenere Cipher encrypts each letter by shifting it according to the corresponding letter of a repeating keyword, and decryption reverses the same process.
for e.g: lets say our key is 'abcd' , and our message is 'ccccccccccc'
so our encrypted text will be: 'cdefcdefcde' and decrypted text will be 'cbazcbazcba'
for 'a' in the key the letter shift by 1
for 'b' in the key the letter shift by 2
.
.
for 'z' in the key the letter shift by 26
thi is how vigenere cipher works 


DESCRIPTION:
its a simple vigenere based encryption/decryption python program where you input text or a txt file path address and it gives you encrypted/decrypted text string/ file according to your selection.

FEATURES:
It askes the user weather to encrypt or decrypt the message
It asks the user for the "key" upon which the whole cryptography works
it works on both txt files and text string input by the user 

USAGE:
you can run the python file in either python interpreter or in terminal by using python vigenere.py or python3 vigenere.py 
upon hitting 'run', the program will ask you weather you want to encrypt or decrypt your message, for encrypting press 'e', for decrypting press 'd', then it'll ask u weather if you wanna use txt fil for or input text string for the cryptography, enter 'f' for file and 't' if you want to input text string.
it will now ask you for key, enter the key
enter text string/ enter relative file path address
your encrypted/decrypted text will be displayed or your encrypted/decrypted file will be saved as "encrypted.txt" or "decrypted.txt" respectively in /Documents/
