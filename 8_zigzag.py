def zigzag_encode(text, key):
    text = text.replace(" ", "")  # Boşlukları kaldır

    if key == 1:  # Eğer sadece 1 satır varsa, metin doğrudan döndürülür
        return text

    # Matris oluştur
    matrix = [['' for _ in range(len(text))] for _ in range(key)]
    
    # Zigzag desenine göre metni matrise yerleştir
    row, direction = 0, 1
    for i in range(len(text)):
        matrix[row][i] = text[i]
        if row == 0:
            direction = 1
        elif row == key - 1:
            direction = -1
        row += direction
    
    # Matristen şifrelenmiş metni oluştur
    encoded_text = ''
    for i in range(key):
        for j in range(len(text)):
            if matrix[i][j] != '':
                encoded_text += matrix[i][j]
    
    return encoded_text

def zigzag_decode(encoded_text, key):
    encoded_text = encoded_text.replace(" ", "")  # Boşlukları kaldır

    if key == 1:  # Eğer sadece 1 satır varsa, metin doğrudan döndürülür
        return encoded_text

    # Matris oluştur
    matrix = [['' for _ in range(len(encoded_text))] for _ in range(key)]
    
    # Zigzag desenine göre matrise şifrelenmiş metni yerleştir
    row, direction = 0, 1
    for i in range(len(encoded_text)):
        matrix[row][i] = '*'
        if row == 0:
            direction = 1
        elif row == key - 1:
            direction = -1
        row += direction
    
    # Matristen çözülmüş metni oluştur
    index = 0
    for i in range(key):
        for j in range(len(encoded_text)):
            if matrix[i][j] == '*' and index < len(encoded_text):
                matrix[i][j] = encoded_text[index]
                index += 1
    
    decoded_text = ''
    row, direction = 0, 1
    for i in range(len(encoded_text)):
        decoded_text += matrix[row][i]
        if row == 0:
            direction = 1
        elif row == key - 1:
            direction = -1
        row += direction
    
    return decoded_text

def main():
    operation = input("Would you like to encrypt or decrypt? (encrypt/decrypt): ").lower()
    if operation == 'e':
        text = input("Enter the text to encrypt: ")
        key = int(input("Enter the number of rows in the zigzag pattern: "))
        encrypted_text = zigzag_encode(text, key)
        print("Encrypted Text:", encrypted_text)
    elif operation == 'd':
        text = input("Enter the text to decrypt: ")
        key = int(input("Enter the number of rows in the zigzag pattern: "))
        decrypted_text = zigzag_decode(text, key)
        print("Decrypted Text:", decrypted_text)
    else:
        print("Invalid operation! Please choose 'encrypt' or 'decrypt'.")

if __name__ == "__main__":
    main()
