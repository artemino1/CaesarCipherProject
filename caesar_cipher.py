# Function to encrypt the given text using the Caesar Cipher
def encrypt(text, shift):
    # Initialize an empty string to store the result
    result = ""
    
    # Loop through each character in the input text
    for char in text:
        # Check if the character is an alphabet (either uppercase or lowercase)
        if char.isalpha():
            # Determine the ASCII value base (65 for uppercase, 97 for lowercase)
            shift_amount = 65 if char.isupper() else 97

            # Encrypt the character by shifting it within the alphabet
            # ord(char) gives the ASCII value of char
            # Subtracting shift_amount makes 'A' or 'a' align to 0
            # Adding the shift value and using modulo 26 keeps it within the alphabet range
            # Adding shift_amount back shifts it to the correct ASCII range
            result += chr((ord(char) + shift - shift_amount) % 26 + shift_amount)
        else:
            # If the character is not an alphabet (like punctuation or space), don't change it
            result += char

    # Return the final encrypted string
    return result

# Function to decrypt the given ciphertext using the Caesar Cipher
# Decryption is just encryption with a negative shift
def decrypt(ciphertext, shift):
    # Call the encrypt function with a negative shift to decrypt
    return encrypt(ciphertext, -shift)

# Main function to run the Caesar Cipher program
def main():
    # Ask the user whether they want to encrypt or decrypt
    choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").upper()

    # Prompt the user to enter the text they want to encrypt or decrypt
    text = input("Enter the text: ")

    # Ask the user for the shift number (key) for the cipher
    shift = int(input("Enter the shift number: "))

    # If the user chose to encrypt
    if choice == 'E':
        # Encrypt the text and print the result
        print("Encrypted Text: ", encrypt(text, shift))
    # If the user chose to decrypt
    elif choice == 'D':
        # Decrypt the text and print the result
        print("Decrypted Text: ", decrypt(text, shift))
    else:
        # If the user entered an invalid choice
        print("Invalid choice!")

# This checks if the script is being run directly (not imported as a module)
# and calls the main function
if __name__ == "__main__":
    main()


