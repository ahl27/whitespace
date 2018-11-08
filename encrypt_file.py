def encrypt(fname, output):
    write_string = ''
    with open(fname) as f:
        for line in f:
            for ch in line:
                write_char = ''
                write_char += '   '
                bitstring = bin(ord(ch))[2:]
                for char in bitstring:
                    if char == '1':
                        write_char += '\t'
                    elif char == '0':
                        write_char += ' '
                write_char += '\n' #terminates number
                write_char += '\t\n  ' #prints character
                write_string += write_char

            write_string += '   \t \t \n\t\n  ' #adds a newline character
        write_string += '\n\n\n' #terminates the program

    with open(output, 'w') as f:
        f.write(write_string)

    print("Successfully wrote text to " + output)
