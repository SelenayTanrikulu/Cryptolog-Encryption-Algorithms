import random

# Alfabe oluşturma fonksiyonu
def create_alphabet(start_char, end_char):
    alphabet = []
    for char in range(ord(start_char), ord(end_char)+1):
        alphabet.append(chr(char))
    return alphabet

# Matris oluşturma fonksiyonu
def create_matrix(data, rows, cols):
    matrix = []
    for i in range(0, len(data), cols):
        matrix.append(data[i:i + cols])
    return matrix

# Kullanıcı girişini şifreleme fonksiyonu
def encrypt_message(message, original_alphabet, shuffled_alphabet):
    encrypted_message = ""
    for i in range(0, len(message), 2):
        first_char, second_char = message[i], message[i+1]
        
        # İlk karakterin koordinatlarını bulma
        for j in range(len(original_alphabet)):
            if first_char in original_alphabet[j]:
                first_row, first_col = j, original_alphabet[j].index(first_char)
                break
        
        # İkinci karakterin koordinatlarını bulma
        for j in range(len(original_alphabet)):
            if second_char in original_alphabet[j]:
                second_row, second_col = j, original_alphabet[j].index(second_char)
                break
        
        # Şifreli karakterleri bulma
        encrypted_first_char = shuffled_alphabet[first_row][second_col]
        encrypted_second_char = shuffled_alphabet[second_row][first_col]
        
        encrypted_message += encrypted_first_char + encrypted_second_char
    
    return encrypted_message

# Kullanıcı girişini çözme fonksiyonu
def decrypt_message(encrypted_message, original_alphabet, shuffled_alphabet):
    decrypted_message = ""
    for i in range(0, len(encrypted_message), 2):
        first_char, second_char = encrypted_message[i], encrypted_message[i+1]
        
        # İlk karakterin koordinatlarını bulma
        for row in range(len(shuffled_alphabet)):
            if first_char in shuffled_alphabet[row]:
                first_row, first_col = row, shuffled_alphabet[row].index(first_char)
                break
        
        # İkinci karakterin koordinatlarını bulma
        for row in range(len(shuffled_alphabet)):
            if second_char in shuffled_alphabet[row]:
                second_row, second_col = row, shuffled_alphabet[row].index(second_char)
                break
        
        # Şifreli karakterlerin orijinal karakterlerini bulma
        decrypted_first_char = original_alphabet[first_row][second_col]
        decrypted_second_char = original_alphabet[second_row][first_col]
        
        decrypted_message += decrypted_first_char + decrypted_second_char
    
    return decrypted_message

# Ana kod
if __name__ == "__main__":
    # Orijinal ve karıştırılmış alfabe oluşturma
    original_alphabet = create_matrix(create_alphabet('a', 'y'), 5, 5)
    shuffled_alphabet = create_matrix(random.sample(create_alphabet('a', 'y'), 25), 5, 5)
    
    # Kullanıcı girişi
    choice = input("Enter 'e' to encrypt or 'd' to decrypt: ")
    if choice == 'e':
        message = input("Şifrelenecek ifadeyi girin: ")
        # Eğer mesajın uzunluğu tek ise, son karaktere rastgele bir harf ekle
        if len(message) % 2 != 0:
            message += random.choice(create_alphabet('a', 'y'))
        
        # Mesajı şifreleme
        encrypted_message = encrypt_message(message, original_alphabet, shuffled_alphabet)
        print("Şifrelenmiş Mesaj:", encrypted_message)
    elif choice == 'd':
        encrypted_message = input("Çözülecek şifreli ifadeyi girin: ")
        decrypted_message = decrypt_message(encrypted_message, original_alphabet, shuffled_alphabet)
        print("Çözülmüş Mesaj:", decrypted_message)
    else:
        print("Geçersiz seçim!")
