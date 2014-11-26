import hashlib
import tkinter.messagebox
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
    fo = open(file_location, "w")
    fo.write(data)
    fo.close()
    
#
# To use, import useful and then use useful.writeline("file location", "data")
#
# This function writes a line to the specified file
def writeline(file_location, data):
    fo = open(file_location, "w")
    fo.write(data + "\n")
    fo.close()

#
# To use, import useful and then use useful.append_file("file location", "data")
#
def append_file(file_location, data):
    with open(file_location, "a") as myfile:
        myfile.write(data)

#
# To use, import useful and then use useful.appendline("file location", "data")
#
def appendline(file_location, data):
    with open(file_location, "a") as myfile:
        myfile.write(data + "\n")
#
# To use, import useful and then use useful.showinfo("Message") - a title doesn't have to be defined.
#
def showinfo(message, title=""):
    tkinter.messagebox.showinfo(title,message)
def showerror(message, title=""):
    tkinter.messagebox.showerror(title,message)            
