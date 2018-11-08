from whitespace_fxns import *
from stack import Stack

def decrypt(fname, g):
    bytestring = ''
    with open(fname) as f:
        for line in f:
            for ch in line:
                if ord(ch) == 32:
                    bytestring += '0'
                elif ord(ch) == 9:
                    bytestring += '1'
            bytestring += '2'
    ##return bytestring
    g.bytestring = bytestring

    #0 is space, 1 is tab, 2 is carraige return
    while g.bytestring:
        #print(g.bytestring[g.i:])
        if g.bytestring[g.i] == '0':
            #stack manipulation
            g.i += 1
            stack_manipulation(g)

        elif g.bytestring[g.i:g.i + 2] == '10':
            #arithmetic
            g.i += 2
            arithmetic(g)

        elif g.bytestring[g.i:g.i+2] == '11':
            #heap access
            g.i += 2
            heap_access(g)

        elif g.bytestring[g.i] == '2':
            #Flow Control
            g.i += 1
            flow_control(g)
            if g.exit:
                #exit the program
                break

        elif g.bytestring[g.i:g.i+2] == '12':
            #I/O
            g.i += 2
            io(g)

    if not g.exit:
        print("ERROR: Reached end of program without termination signal")