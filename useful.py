import hashlib
import tkinter.messagebox
### To use, please import useful ###

# -------- useful.encrypt(string data) --------
#
# You can use this function to ENCRYPT strings...
# ============================================
# For example; if you're creating a login system and you wish to encrypt the password you simply get the inputted password
# (in this example we shall store it in IN_PASS), encrypt it and compare it to a pre-encrypted saved password (usually stored in a text file)
# (we shall stored the pre-encrypted saved password in ENC_PASS)
#
#     ###########################################
#    # IN_PASS = "password"                      #
#    # ENC_PASS = useful.read_file("example.txt")#
#    # if ENC_PASS==useful.encrypt(IN_PASS):     #
#    #       useful.showinfo("It matches!")      #
#    # else:                                     #
#    #       useful.showerror("Not a match!")    #
#     ###########################################
#
# ============================================
# Use:
#   useful.encrypt("text to be encrypted")
# ============================================
def encrypt(text):
    return hashlib.sha224(text.encode('utf-8')).hexdigest()



# -------- useful.read_file(string location) --------
#
# You can use this function to read the ENTIRE contents of a file...
# ============================================
# For example; to open the file `info.txt` (presuming it's in the same directory as the program) and load it's contents into the variable INFO_CONTENTS, use:
#
#     #############################################
#    # INFO_CONTENTS = useful.read_file("info.txt")#
#     #############################################
#
# ============================================
# Use:
#       useful.read_file("file location")
#
def read_file(file_location):
    fo = open(file_location, "r+")
    str = fo.read()
    fo.close()
    return str



# -------- useful.write_file(string location, data) --------
#
# You can use this function to write contents to a file...
# ============================================
# For example; to write the file `info.txt` (presuming it's in the same directory as the program) and with the data stored in FILE_CONTENTS, do:
#
#     #############################################
#    # useful.write_file("info.txt",FILE_CONTENTS) #
#     #############################################
#
# ============================================
# Use:
#       useful.write_file("file location", "data")
#
def write_file(file_location, data):
    fo = open(file_location, "w")
    fo.write(data)
    fo.close()
    


# -------- useful.writeline(string location, string data) --------
#
# You can use this function to write contents to a file with a trailer new line
# ============================================
# For example; to write the file `info.txt` (presuming it's in the same directory as the program) and with the data stored in FILE_CONTENTS, do:
#
#     #############################################
#    # useful.writeline("info.txt",FILE_CONTENTS)  #
#     #############################################
#
# ============================================
# Use:
#       useful.writeline("file location", "data")
#
def writeline(file_location, data):
    fo = open(file_location, "w")
    fo.write(data + "\n")
    fo.close()



# -------- useful.append_file(string location, string data) --------
#
# You can use this function to append data to a file...
# ============================================
# For example; to append the file `info.txt` (presuming it's in the same directory as the program) and with the data stored in FILE_CONTENTS, do:
#
#     #############################################
#    # useful.append_file("info.txt",FILE_CONTENTS)#
#     #############################################
#
# ============================================
# Use:
#       useful.append_file("file location", "data")
#
def append_file(file_location, data):
    with open(file_location, "a") as myfile:
        myfile.write(data)



# -------- useful.appendline(string location, string data) --------
#
# You can use this function to append data to a file with a trailer new line
# ============================================
# For example; to append the file `info.txt` (presuming it's in the same directory as the program) and with the data stored in FILE_CONTENTS, do:
#
#     #############################################
#    # useful.appendline("info.txt", FILE_CONTENTS)#
#     #############################################
#
# ============================================
# Use:
#       useful.appendline("file location", "data")
#
def appendline(file_location, data):
    with open(file_location, "a") as myfile:
        myfile.write(data + "\n")


        
# -------- useful.showinfo(string message, string title) --------
#
# You can use this function to show a information message box
# ============================================
# For example; to show a messsage do the following:
#
#     #############################################
#    # useful.showinfo("Hello world!")             #
#     #############################################
#
# ============================================
# Use:
#       useful.showinfo("Message", "Title")
#
def showinfo(message, title=""):
    tkinter.messagebox.showinfo(title,message)


    
# -------- useful.showerror(string message, string title) --------
#
# You can use this function to show an error message box
# ============================================
# For example; to show a messsage do the following:
#
#     #############################################
#    # useful.showerror("You messed up!")           #
#     #############################################
#
# ============================================
# Use:
#       useful.showerror("Message", "Title")
#
def showerror(message, title=""):
    tkinter.messagebox.showerror(title,message)            
