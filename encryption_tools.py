from cryptography.fernet import Fernet

def generate_key():
    """Generate kunci enkripsi."""
    return Fernet.generate_key()

def encrypt_data(data, key):
    """Enkripsi data sensitif."""
    cipher = Fernet(key)
    return cipher.encrypt(data.encode())

def decrypt_data(encrypted_data, key):
    """Dekripsi data."""
    cipher = Fernet(key)
    return cipher.decrypt(encrypted_data).decode()

# Contoh penggunaan:
# key = generate_key()
# encrypted = encrypt_data("Secret Message", key)
# decrypted = decrypt_data(encrypted, key)