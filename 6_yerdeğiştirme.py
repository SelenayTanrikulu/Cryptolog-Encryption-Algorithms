def encrypt(text, key):
    # Metni parçalara böler, her parça anahtar uzunluğu kadar olacak şekilde ayarlanır
    chunks = [text[i:i + key] for i in range(0, len(text), key)]
    
    # Eğer son parça anahtar uzunluğundan kısa ise 'a' karakteri ile doldurulur
    last_chunk_len = len(chunks[-1])
    if last_chunk_len < key:
        chunks[-1] += 'a' * (key - last_chunk_len)
    
    # Şifrelenmiş metni oluşturur
    encrypted_text = ''
    for i in range(key):
        for chunk in chunks:
            encrypted_text += chunk[i]
    
    return encrypted_text

def decrypt(encrypted_text, key):
    # Metni parçalara böler, her parça anahtar uzunluğu kadar olacak şekilde ayarlanır
    chunks = [encrypted_text[i:i + len(encrypted_text) // key] for i in range(0, len(encrypted_text), len(encrypted_text) // key)]
    
    # Şifrelenmiş metni çözer
    decrypted_text = ''
    for i in range(len(chunks[0])):
        for chunk in chunks:
            decrypted_text += chunk[i]
    
    return decrypted_text

def main():
    choice = input("Enter 'e' to encrypt or 'd' to decrypt: ")
    if choice == 'e':
        text = input("Enter the text to encrypt: ")
        text = text.replace(" ", "")
        key = int(input("Enter the key (number of columns): "))
        encrypted_text = encrypt(text, key)
        print("Encrypted Text:", encrypted_text)
    elif choice == 'd':
        encrypted_text = input("Enter the encrypted text: ")
        encrypted_text = encrypted_text.replace(" ", "")
        key = int(input("Enter the key (number of columns): "))
        decrypted_text = decrypt(encrypted_text, key)
        print("Decrypted Text:", decrypted_text)
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()