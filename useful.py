import hashlib

#
# To use, import useful and then use useful.encrypt("text to be encrypted")
#
def encrypt(text):
    return hashlib.sha224(text.encode('utf-8')).hexdigest()

#
# To use, import useful and then use useful.read_file("file location")
#
def read_file(file_location):
    fo = open(file_location, "r+")
    str = fo.read()
    fo.close()
    return str
