from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import binascii

# AES Encryption function
def aes_encrypt(plaintext, key):
    key = key.encode('utf-8')  # Convert key to bytes
    plaintext = plaintext.encode('utf-8')  # Convert plaintext to bytes
    cipher = AES.new(key, AES.MODE_CBC)  # Create AES cipher in CBC mode
    ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))  # Encrypt and pad
    return binascii.hexlify(cipher.iv + ciphertext).decode('utf-8')  # Include IV

# AES Decryption function
def aes_decrypt(ciphertext, key):
    key = key.encode('utf-8')
    ciphertext = binascii.unhexlify(ciphertext)  # Convert hex back to bytes
    iv = ciphertext[:AES.block_size]  # Extract IV
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_text = unpad(cipher.decrypt(ciphertext[AES.block_size:]), AES.block_size)
    return decrypted_text.decode('utf-8')

# Example Usage
key = "thisisasecretkey"  # Must be 16, 24, or 32 bytes long
plaintext = "HELLO WORLD"

encrypted_text = aes_encrypt(plaintext, key)
decrypted_text = aes_decrypt(encrypted_text, key)

print("Plaintext:", plaintext)
print("Encrypted Text:", encrypted_text)
print("Decrypted Text:", decrypted_text)
