import numpy as np

def text_to_numbers(text):
    return [ord(char) - ord('A') for char in text.upper()]

def numbers_to_text(numbers):
    return ''.join(chr(num + ord('A')) for num in numbers)

def hill_encrypt(plaintext, key_matrix):
    n = len(key_matrix)
    plaintext = plaintext.upper().replace(" ", "")

    # Padding if needed
    while len(plaintext) % n != 0:
        plaintext += "X"

    plaintext_numbers = text_to_numbers(plaintext)
    ciphertext_numbers = []

    for i in range(0, len(plaintext_numbers), n):
        block = np.array(plaintext_numbers[i:i+n])
        encrypted_block = np.dot(key_matrix, block) % 26
        ciphertext_numbers.extend(encrypted_block)

    return numbers_to_text(ciphertext_numbers)

# Example Usage
key_matrix = np.array([[3, 3], [2, 5]])  # 2x2 Key Matrix
plaintext = "OKAY"

encrypted_text = hill_encrypt(plaintext, key_matrix)
print("Encrypted Text:", encrypted_text)
