import hashlib

def encrypt(text):
    return hashlib.sha224(text.encode('utf-8')).hexdigest()
