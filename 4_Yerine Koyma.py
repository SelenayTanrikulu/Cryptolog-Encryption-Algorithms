def encrypt(text):
    turkish_alphabet = 'abcçdefgğhıijklmnoöprsştuüvyz'
    mixed_alphabet = 'zyvüutşsrpöonmlkjiıhğgfedçcba'
    encrypted_text = ''
    text = text.replace(" ", "")

    for char in text:
        if char.isalpha():
            if char.islower():
                index = turkish_alphabet.find(char)
                encrypted_text += mixed_alphabet[index]
            else:
                index = turkish_alphabet.find(char.lower())
                encrypted_text += mixed_alphabet[index].upper()
        else:
            encrypted_text += char

    return encrypted_text

def decrypt(encrypted_text):
    turkish_alphabet = 'abcçdefgğhıijklmnoöprsştuüvyz'
    mixed_alphabet = 'zyvüutşsrpöonmlkjiıhğgfedçcba'
    decrypted_text = ''

    for char in encrypted_text:
        if char.isalpha():
            if char.islower():
                index = mixed_alphabet.find(char)
                decrypted_text += turkish_alphabet[index]
            else:
                index = mixed_alphabet.find(char.lower())
                decrypted_text += turkish_alphabet[index].upper()
        else:
            decrypted_text += char

    return decrypted_text

def main():
    choice = input("Enter 'e' to encrypt a message, 'd' to decrypt: ")
    if choice == 'e':
        text = input("Enter the message to encrypt: ")
        text = text.replace(" ", "")
        print("Encrypted Text:", encrypt(text))
    elif choice == 'd':
        encrypted_text = input("Enter the encrypted message: ")
        encrypted_text = encrypted_text.replace(" ", "")
        print("Decrypted Text:", decrypt(encrypted_text))
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()