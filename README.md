# Caesar Cipher Project

This project demonstrates the Caesar Cipher, a basic encryption technique used in cryptography. The script can encrypt and decrypt messages using a specified shift value. For example, with a shift of 3, **A** would be encrypted to **D**, **B** to **E**, and so on.

## Language used

Bash, Python

## Environment used

Linux

## Program walk-through

1. We created a new directory for our project in the terminal on our VM and initialized a new Git repository. After that, we crafted a Python file `caesar_cipher.py` (you may dive into it and read the listed comments). 

![](https://imgur.com/uUuQwRO.png)


2. Now let's try different strings and shift values to ensure the encryption and decryption functions work as expected.

![](https://imgur.com/aRjfiJI.png)
![](https://imgur.com/WIWVQFW.png)


## Summary

- `encrypt(text, shift)`: Encrypts the input text by shifting each letter by shift positions.
- `decrypt(ciphertext, shift)`: Decrypts the ciphertext by shifting each letter back by shift positions.
- `main()`: Handles user input and decides whether to encrypt or decrypt based on the user's choice.
