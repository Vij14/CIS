from Crypto.Cipher import DES
import binascii

# Function to pad the text to be multiple of 8 bytes (DES block size)
def pad(text):
    while len(text) % 8 != 0:
        text += " "
    return text

# DES Encryption function
def des_encrypt(plaintext, key):
    key = key.encode('utf-8')  # Convert key to bytes
    plaintext = pad(plaintext).encode('utf-8')  # Convert plaintext to bytes
    
    cipher = DES.new(key, DES.MODE_ECB)  # Create DES cipher in ECB mode
    encrypted_text = cipher.encrypt(plaintext)  # Encrypt the text
    return binascii.hexlify(encrypted_text).decode('utf-8')  # Convert to hex string

# DES Decryption function
def des_decrypt(ciphertext, key):
    key = key.encode('utf-8')
    ciphertext = binascii.unhexlify(ciphertext)  # Convert hex string back to bytes
    
    cipher = DES.new(key, DES.MODE_ECB)
    decrypted_text = cipher.decrypt(ciphertext).decode('utf-8').strip()  # Remove padding
    return decrypted_text

# Example Usage
key = "8BYTEKEY"  # DES requires an 8-byte key
plaintext = "HELLO123"

encrypted_text = des_encrypt(plaintext, key)
decrypted_text = des_decrypt(encrypted_text, key)

print("Plaintext:", plaintext)
print("Encrypted Text:", encrypted_text)
print("Decrypted Text:", decrypted_text)
