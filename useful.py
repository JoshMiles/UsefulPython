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

#
# To use, import useful and then use useful.write_file("file location", "data")
#
def write_file(file_location, data):
    fo = open(file_location, "wb")
    fo.write(data)
    fo.close()


#
# To use, import useful and then use useful.rappend_file("file location", "data")
#
def append_file(file_location, data):
    with open(file_location, "a") as myfile:
        myfile.write(data)
