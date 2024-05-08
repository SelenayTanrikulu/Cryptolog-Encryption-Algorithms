def inverse_permutation(permutation):
    # Permutasyonun tersini alır
    inverse = [''] * len(permutation)
    for i, char in enumerate(permutation):
        inverse[int(char)-1] = str(i+1)
    return ''.join(inverse)

def permute(text, key, permutation):
    # Metni parçalara böler
    text = text.replace(" ", "")
    chunks = [text[i:i+key] for i in range(0, len(text), key)]
    # Eksik karakterleri 'a' ile doldurur
    for i in range(len(chunks[-1]), key):
        chunks[-1] += 'a'
    # Şifrelenmiş metni tutmak için boş bir string oluşturur
    encrypted_text = ''

    # Her parça için permütasyon uygular
    for chunk in chunks:
        # Parçadaki karakterlerin sırasını değiştirmek için permütasyonu kullanır
        permuted_chunk = ''
        for i in range(len(permutation)):
            index = int(permutation[i]) - 1
            if index < len(chunk):
                permuted_chunk += chunk[index]
        # Şifrelenmiş metne ekler
        encrypted_text += permuted_chunk

    return encrypted_text

def unpermute(encrypted_text, key, permutation):
    # Metni parçalara böler
    encrypted_text = encrypted_text.replace(" ", "")
    chunks = [encrypted_text[i:i+key] for i in range(0, len(encrypted_text), key)]
    # Eksik karakterleri 'a' ile doldurur
    for i in range(len(chunks[-1]), key):
        chunks[-1] += 'a'
    # Çözülmüş metni tutmak için boş bir string oluşturur
    decrypted_text = ''

    # Her parça için ters permütasyon uygular
    for chunk in chunks:
        # Parçadaki karakterlerin sırasını değiştirmek için ters permütasyonu kullanır
        unpermuted_chunk = ''
        inverse = inverse_permutation(permutation)
        for i in range(len(inverse)):
            index = int(inverse[i]) - 1
            if index < len(chunk):
                unpermuted_chunk += chunk[index]
        # Çözülmüş metne ekler
        decrypted_text += unpermuted_chunk

    return decrypted_text

def main():
    choice = input("Enter 'e' to encrypt or 'd' to decrypt: ")
    text = input("Enter the text: ")
    key = int(input("Enter the key length: "))
    permutation = input("Enter the permutation (e.g., 32541): ")

    # Permütasyon anahtarının doğruluğunu kontrol eder
    if sorted(permutation) != sorted([str(i) for i in range(1, key + 1)]):
        print("Invalid permutation key!")
        return

    if choice == 'e':
        encrypted_text = permute(text, key, permutation)
        print("Encrypted Text:", encrypted_text)
    elif choice == 'd':
        decrypted_text = unpermute(text, key, permutation)
        print("Decrypted Text:", decrypted_text)
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()

