from Crypto import Random
from Crypto.Cipher import AES
import os
import os.path
from os import listdir
from os.path import isfile, join


class Encryptor:
    def __init__(self, key):
        self.key = key

    def pad(self, s):
        return s + b"\0" * (AES.block_size - len(s) % AES.block_size)

    def encrypt(self, message, key, key_size=256):
        message = self.pad(message)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        return iv + cipher.encrypt(message)

    def encrypt_file(self, file_name):
        with open(file_name, 'rb') as fo:
            plaintext = fo.read()
        enc = self.encrypt(plaintext, self.key)
        with open(file_name + ".enc", 'wb') as fo:
            fo.write(enc)
        os.remove(file_name)

    def decrypt(self, ciphertext, key):
        iv = ciphertext[:AES.block_size]
        cipher = AES.new(key, AES.MODE_CBC, iv)
        plaintext = cipher.decrypt(ciphertext[AES.block_size:])
        return plaintext.rstrip(b"\0")

    def decrypt_file(self, file_name):
        with open(file_name, 'rb') as fo:
            ciphertext = fo.read()
        dec = self.decrypt(ciphertext, self.key)
        with open(file_name[:-4], 'wb') as fo:
            fo.write(dec)
        os.remove(file_name)

    def getAllFiles(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        dirs = []
        for dirName, subdirList, fileList in os.walk(dir_path):
            for fname in fileList:
                if fname != 'code.py':
                    dirs.append(dirName + "\\" + fname)
        return dirs

    def encrypt_all_files(self):
        dirs = self.getAllFiles()
        for file_name in dirs:
            self.encrypt_file(file_name)

    def decrypt_all_files(self):
        dirs = self.getAllFiles()
        for file_name in dirs:
            self.decrypt_file(file_name)


key = ['garbage',b'\xbf\xc0\x85)\x10nc\x94\x02)j\xdf\xcb\xc4\x94\x9d(\x9e[EX\xc8\xd5\xbfI{\xa2$\x05(\xd5\x99', b'\xbf\xc0\x85)\x10nc\x94\x02)j\xdf\xcb\xc4\x94\x9d(\x9e[EX\xc8\xd5\xbfI{\xa2$\x05(\xd5\x18', b'\xbf\xc0\x85)\x10nc\x94\x02)j\xdf\xcb\xc4\x94\x9d(\x9e[EX\xc8\xd5\xbfI{\xa2$\x05(\xd5\x69', b'[EX\xc8\xd5\xbfI{\xa2$\x05(\xd5\x18\xbf\xc0\x85)\x10nc\x94\x02)j\xdf\xcb\xc4\x94\x9d(\x9e']
# key =b'\xbf\xc0\x85)\x10nc\x94\x02)j\xdf\xcb\xc4\x94\x9d(\x9e[EX\xc8\xd5\xbfI{\xa2$\x05(\xd5\x99'
# key  = bytes(key,encoding='utf-8')
# key = k.encode('UTF-8')
# print(key)
defaultEnc = Encryptor(key[1])
clear = lambda: os.system('cls')

curr = 1


def menuloop(curr):

    clear()
    print("-----------Key in use => KEY "+str(curr)+"-----------\n")
    want = str(input("Do you want to change current key of AES (Y/N)?\n"))

    if want == "Y":

        f = True
        while f==True:
            curr = int(input("\nKEY MENU\n1. Enter '1' to select KEY 1.\n2. Enter '2' to select KEY 2.\n3. Enter '3' to select KEY 3.\n4. Enter '4' to select KEY 4.\n"))
            # print(curr)
            if curr<=4 and curr>=1:
                enc = Encryptor(key[curr])
                f = False
            else:
                print("Please select a valid option!") 
            

        # print(newKey)
        
            
        while True:        
            clear()
            print("-----------Key in use => KEY "+str(curr)+"-----------\n")
            choice = int(input(
                "1. Press '1' to encrypt file.\n2. Press '2' to decrypt file.\n3. Press '3' to Encrypt all files in the directory.\n4. Press '4' to decrypt all files in the directory.\n5. Press '5' to select key.\n6. Press '6' to exit.\n"))
            clear()
            
            if choice == 1:
                enc.encrypt_file(str(input("Enter name of file to encrypt: ")))
            elif choice == 2:
                enc.decrypt_file(str(input("Enter name of file to decrypt: ")))
            elif choice == 3:
                enc.encrypt_all_files()
            elif choice == 4:
                enc.decrypt_all_files()
            elif choice == 5:
                menuloop(curr)
                exit()
            elif choice == 6:
                exit()
            else:
                print("Please select a valid option!")

    else:
            
        while True:           
            clear()
            print("-----------Key in use => KEY "+str(curr)+"-----------\n")
            choice = int(input(
                "1. Press '1' to encrypt file.\n2. Press '2' to decrypt file.\n3. Press '3' to Encrypt all files in the directory.\n4. Press '4' to decrypt all files in the directory.\n5. Press '5' to select key.\n6. Press '6' to exit.\n"))
            clear()
            
            if choice == 1:
                defaultEnc.encrypt_file(str(input("Enter name of file to encrypt: ")))
            elif choice == 2:
                defaultEnc.decrypt_file(str(input("Enter name of file to decrypt: ")))
            elif choice == 3:
                defaultEnc.encrypt_all_files()
            elif choice == 4:
                defaultEnc.decrypt_all_files()
            elif choice == 5:
                menuloop(curr)
                exit()
            elif choice == 6:
                exit()
            else:
                print("Please select a valid option!")    

    

clear()
print("COMPUTER NETWORK PROJECT\n")
print("Made By:\nTejas Harish Borkar 2K18/CO/373\nTushar Ahuja        2K18/CO/374")
str(input(""))

menuloop(curr)