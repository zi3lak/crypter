from flask import Flask, request, render_template
from cryptography.fernet import Fernet, InvalidToken
import base64

app = Flask(__name__)

def generate_key():
    # Generuj klucz Fernet
    key = Fernet.generate_key()
    return key

def generate_fernet(key):
    return Fernet(key)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_key', methods=['GET', 'POST'])
def generate_key_page():
    if request.method == 'POST':
        key = generate_key()
        url_safe_key = key.decode()  # Poprawienie kodowania klucza
        return render_template('index.html', generated_key=url_safe_key)
    return render_template('index.html')

@app.route('/encrypt', methods=['POST'])
def encrypt():
    message_to_encrypt = request.form['message']
    user_key = request.form['encryption_key']  # Pobierz klucz od użytkownika
    try:
        fernet = generate_fernet(user_key)
        encrypted_message = fernet.encrypt(message_to_encrypt.encode())
        return render_template('result.html', message=encrypted_message, user_key=user_key, operation='Szyfrowanie')
    except Exception as e:
        return render_template('result.html', error_message=str(e), user_key=user_key, operation='Szyfrowanie')

@app.route('/decrypt', methods=['POST'])
def decrypt():
    encrypted_message = request.form['encrypted_message']
    user_key = request.form['decryption_key']  # Pobierz klucz od użytkownika
    try:
        fernet = generate_fernet(user_key)
        decrypted_message = fernet.decrypt(encrypted_message.encode()).decode()
        return render_template('result.html', message=decrypted_message, user_key=user_key, operation='Deszyfrowanie')
    except InvalidToken:
        return render_template('result.html', error_message='Nieprawidłowy klucz odszyfrowywania', user_key=user_key, operation='Deszyfrowanie')
    except Exception as e:
        return render_template('result.html', error_message=str(e), user_key=user_key, operation='Deszyfrowanie')

if __name__ == '__main__':
    app.run(debug=True)






