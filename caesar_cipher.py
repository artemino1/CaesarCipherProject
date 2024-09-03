def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = 65 if char.isupper() else 97
            result += chr((ord(char) + shift - shift_amount) % 26 + shift_amount)
        else:
            result += char
    return result

def decrypt(ciphertext, shift):
    return encrypt(ciphertext, -shift)

def main():
    choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").upper()
    text = input("Enter the text: ")
    shift = int(input("Enter the shift number: "))

    if choice == 'E':
        print("Encrypted Text: ", encrypt(text, shift))
    elif choice == 'D':
        print("Decrypted Text: ", decrypt(text, shift))
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()


