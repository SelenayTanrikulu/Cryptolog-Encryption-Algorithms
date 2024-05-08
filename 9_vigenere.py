def vigenere_encrypt(text, key):
    alphabet = 'abcçdefgğhıijklmnoöprsştuüvyz'
    
    # Metinden boşluk karakterlerini kaldır
    text = text.replace(" ", "")
    
    # Anahtar kelimeyi küçük harfe dönüştür
    key = key.lower()
    
    # Anahtar kelimeyi metnin uzunluğuna genişlet
    expanded_key = (key * (len(text) // len(key))) + key[:len(text) % len(key)]
    
    # Şifrelenmiş metni oluştur
    encrypted_text = ''
    for i in range(len(text)):
        text_index = alphabet.find(text[i].lower())
        key_index = alphabet.find(expanded_key[i])
        encrypted_index = (text_index + key_index) % 29
        encrypted_text += alphabet[encrypted_index].upper() if text[i].isupper() else alphabet[encrypted_index]
    
    return encrypted_text

def vigenere_decrypt(encrypted_text, key):
    alphabet = 'abcçdefgğhıijklmnoöprsştuüvyz'
    
    # Anahtar kelimeyi küçük harfe dönüştür
    key = key.lower()
    
    # Anahtar kelimeyi metnin uzunluğuna genişlet
    expanded_key = (key * (len(encrypted_text) // len(key))) + key[:len(encrypted_text) % len(key)]
    
    # Çözülmüş metni oluştur
    decrypted_text = ''
    for i in range(len(encrypted_text)):
        encrypted_index = alphabet.find(encrypted_text[i].lower())
        key_index = alphabet.find(expanded_key[i])
        decrypted_index = (encrypted_index - key_index) % 29
        decrypted_text += alphabet[decrypted_index].upper() if encrypted_text[i].isupper() else alphabet[decrypted_index]
    
    return decrypted_text

def main():
    choice = input("Enter 'e' to encrypt or 'd' to decrypt: ")
    if choice == 'e':
        text = input("Enter the text to encrypt: ")
        key = input("Enter the key (a string word): ")
        encrypted_text = vigenere_encrypt(text, key)
        print("Encrypted Text:", encrypted_text)
    elif choice == 'd':
        encrypted_text = input("Enter the encrypted text: ")
        key = input("Enter the key (a string word): ")
        decrypted_text = vigenere_decrypt(encrypted_text, key)
        print("Decrypted Text:", decrypted_text)
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
