def rotate_matrix(input_str, key):
    # Boşlukları kaldır ve eksik olan yerleri 'X' ile doldur
    input_str = input_str.replace(" ", "")
    remainder = len(input_str) % key
    if remainder > 0:
        input_str += 'X' * (key - remainder)

    # Matris boyutlarını hesapla
    rows = len(input_str) // key
    cols = key

    # Matrisi oluştur
    matrix = [[''] * cols for _ in range(rows)]

    # Matrise harfleri yerleştir
    index = 0
    for i in range(rows):
        for j in range(cols):
            matrix[i][j] = input_str[index]
            index += 1

    # Rota algoritmasını uygula
    result = []
    visited = set()
    i = j = 0
    direction = 0  # 0: sağa, 1: aşağı, 2: sola, 3: yukarı

    while len(result) < len(input_str):
        # Eğer kordinat ziyaret edilmediyse
        if (i, j) not in visited:
            result.append(matrix[i][j])
            visited.add((i, j))
        else:
            break

        # Sağa git
        if direction == 0:
            if j + 1 < cols and (i, j + 1) not in visited:
                j += 1
            else:
                direction = 1
                i += 1
        # Aşağı git
        elif direction == 1:
            if i + 1 < rows and (i + 1, j) not in visited:
                i += 1
            else:
                direction = 2
                j -= 1
        # Sola git
        elif direction == 2:
            if j - 1 >= 0 and (i, j - 1) not in visited:
                j -= 1
            else:
                direction = 3
                i -= 1
        # Yukarı git
        elif direction == 3:
            if i - 1 >= 0 and (i - 1, j) not in visited:
                i -= 1
            else:
                direction = 0
                j += 1

    # Matrisi ekrana yazdır
    print("Matris:")
    for row in matrix:
        print(row)

    return ''.join(result)

def main():
    choice = input("Enter 'e' to encrypt or 'd' to decrypt: ")
    text = input("Enter the text: ")
    key = int(input("Enter the key length (an integer): "))

    if choice == 'e':
        encrypted_text = rotate_matrix(text, key)
        print("Encrypted Text:", encrypted_text)
    elif choice == 'd':
        decrypted_text = rotate_matrix(text, key)
        print("Decrypted Text:", decrypted_text)
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
