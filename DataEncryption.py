from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import base64

# AES encryption with AES-256
def encrypt_data(data, key):
    # Ensure key length is 32 bytes (256 bits)
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(data.encode(), AES.block_size))
    iv = base64.b64encode(cipher.iv).decode('utf-8')
    ct = base64.b64encode(ct_bytes).decode('utf-8')
    return iv, ct

# Example of encrypting patient data
key = get_random_bytes(32)  # AES 256-bit key
patient_data = "Patient ID: 12345, Heart Rate: 75bpm, Oxygen Level: 98%"
iv, encrypted_data = encrypt_data(patient_data, key)

print(f"IV: {iv}")
print(f"Encrypted Data: {encrypted_data}")
