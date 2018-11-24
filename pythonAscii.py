# pythonAscci.py copyright of Parzifalkali. Do NOT copy it as yours

# Import modules

import sys

# End of import modules

# creating the decode and encode functions

def decodeAscii(ascii):
    string = chr(ascii)
    print(string)

def encodeAscii(string):
    for letter in string:
        print(ord(letter))

# End of creating the decode and encode functions

# Executing the program wiht the if __name__ == "__main__": ...

if __name__ == "__main__":
    #Python2 version :

    choice = raw_input("(1 = Decode or 2 = Encode) >> ")

    if choice == "1":
        ascii = int(raw_input("Enter the ascii to decode : >> "))
        decodeAscii(ascii)
        sys.exit()

    if choice == "2":
        string = raw_input("Enter the string to encode : ")
        encodeAscii(string)
        sys.exit()

    elif choice != "1" or "2" :
        print("Commad not found: Exiting ...")
        sys.exit()

    # Python3 version:
    #choice = input("(1 = Decode or 2 = Encode) >> ")

    #if choice == "1":
        #ascii = int(input("Enter the ascii to decode : >> "))
        #decodeAscii(ascii)
        #sys.exit()

    #if choice == "2":
        #string = input("Enter the string to encode : ")
        #encodeAscii(string)
        #sys.exit()

    #elif choice != "1" or "2":
        #print("Commad not found: Exiting ...")
        #sys.exit()

# End of executing the program

# End of the code .