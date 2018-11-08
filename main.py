import argparse
from decrypt_file import *
from encrypt_file import *
from stack import Stack

'''
Class to hold global variables, since I couldn't think of a better way to do it
'''
class Globals:
    labels = {}
    bytestring = ''
    memory = {}
    i = 0
    exit = False


    def __init__(self):
        self.stack = Stack()
        self.prevGlobals = Stack()

    def store(self, copy):
        self.prevGlobals.push(copy)

    def rollback(self):
        old = self.prevGlobals.pop()
        old.copy_vals(self)

    def copy_vals(self, newg):
        newg = Globals()
        newg.labels = self.labels
        newg.subroutine = self.subroutine
        newg.bytestring = self.bytestring
        newg.memory = self.memory
        newg.i = self.i
        newg.exit = self.exit
        newg.stack = self.stack
        newg.prevGlobals = self.prevGlobals
        

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('fname', type=str, help='Filename of textfile to encrypt or .wsp/.txt file to decrypt') #text file to encrypt or whitespace file to decrypt
    parser.add_argument("-d", '--decrypt', action='store_true', help='OPTIONAL: flag to signal decryption') #flag to decrypt
    parser.add_argument('-e', '--encrypt', action='store_true', help='OPTIONAL: flag to signal encryption') #flag to encrypt
    parser.add_argument('-o', '--output', default='converted', help='OPTIONAL: name of output file for encryption. ".wsp" extension added automatically.') #name of file to output to

    args = parser.parse_args()
    print("\n")

    if args.encrypt: #encrypts a message into whitespace
        encrypt(args.fname, args.output)
    if args.decrypt:
        globals = Globals()
        decrypt(args.fname, globals)

    print("\n")

if __name__ == '__main__':
    main()