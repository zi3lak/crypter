from cryptography.fernet import Fernet

# Generuj klucz Fernet
key = Fernet.generate_key()

# Konwertuj klucz do formatu URL-safe base64 i wyświetl go
url_safe_key = key.decode()
print(url_safe_key)
