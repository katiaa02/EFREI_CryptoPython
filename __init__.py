from cryptography.fernet import Fernet
from flask import Flask, render_template_string, render_template, jsonify
from flask import render_template
from flask import json
from urllib.request import urlopen
import sqlite3
import urllib.parse                                                                                                                                       
app = Flask(__name__)   #12                                                                                                               
                                                                                                                                       
@app.route('/')
def hello_world():
    return render_template('hello.html')

key = Fernet.generate_key()
f = Fernet(key)

@app.route('/encrypt/<string:valeur>')
def encryptage(valeur):
    valeur_bytes = valeur.encode()  # Conversion str -> bytes
    token = f.encrypt(valeur_bytes)  # Encrypt la valeur
    return f"Valeur encryptée : {token.decode()}"  # Retourne le token en str
  
@app.route('/decrypt/<string:token>')
def decryptage(token):
    try:
        token_decoded = urllib.parse.unquote_plus(token)
        decrypted_bytes = f.decrypt(token_decoded.encode())
        decrypted = decrypted_bytes.decode()
        return f"Valeur décryptée : {decrypted}"
    except Exception as e:
        return f"Erreur lors du déchiffrement : {str(e)}"

@app.route('/encrypt_personal/<key>/<message>')
def encrypt_personal(key, message):
    try:
        f = Fernet(key.encode())
        encrypted = f.encrypt(message.encode())
        return encrypted.decode()
    except Exception as e:
        return f"Erreur : {str(e)}"

@app.route('/decrypt_personal/<key>/<token>')
def decrypt_personal(key, token):
    try:
        f = Fernet(key.encode())
        decrypted = f.decrypt(token.encode())
        return decrypted.decode()
    except Exception as e:
        return f"Erreur : {str(e)}"


      
if __name__ == "__main__":
  app.run(debug=True)

