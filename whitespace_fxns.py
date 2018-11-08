from main import Globals

def stack_manipulation(g):
    bytestring = g.bytestring
    i = g.i
    stack = g.stack 

    if bytestring[i] == '0':
        #push number
        i += 1
        num, add_i = get_num(bytestring[i:], 0)
        i += add_i
        stack.push(num)
    elif bytestring[i:i+2] == '20':
        #duplicate top item on stack
        obj = stack.pop()
        stack.push(obj)
        stack.push(obj)
        i += 2
    elif bytestring[i:i+2] == '21':
        #swap top two items on stack
        obj1 = stack.pop()
        obj2 = stack.pop()
        stack.push(obj1)
        stack.push(obj2)
        i += 2
    elif bytestring[i:i+2] == '22':
        #discard top item on stack
        stack.pop()
        i += 2
    elif bytestring[i:i+2] == '10':
        #copy N-th item of the stack
        i += 2
        num, i = get_num(bytestring, i)
        stack.push(stack.get_index(i))
    elif bytestring[i:i+2] == '12':
        #slide N items off stack keeping top item
        i += 2
        num, i = get_num(bytestring, i)
        top = stack.pop()
        for j in range(num):
            stack.pop()
        stack.push(top)
    
    g.i = i


def arithmetic(g):
    stack = g.stack
    i = g.i
    bytestring = g.bytestring
    num1 = stack.pop()
    num2 = stack.pop()

    if bytestring[i:i+2] == '00':
        stack.push(num1 + num2)
    elif bytestring[i:i+2] == '01':
        stack.push(num1 - num2)
    elif bytestring[i:i+2] == '02':
        stack.push(num1 * num2)
    elif bytestring[i:i+2] == '10':
        stack.push(num1 // num2)
    elif bytestring[i:i+2] == '11':
        stack.push(num1 % num2)

    g.i = i+2

def heap_access(g):
    ## NOTE: note sure if values are pushed back to the stack after call ##
    bytestring = g.bytestring
    stack = g.stack
    i = g.i
    memory = g.memory

    control = bytestring[i]
    i += 1

    if control == '0':
        #store top element at memory cell given by second pop
        val = stack.pop()
        addr = stack.pop()
        memory[addr] = val

    elif control == '1':
        #retrieve element from address at top value and push to stack
        addr = stack.pop()
        stack.push(memory[addr])

    g.i = i
    g.memory = memory

def flow_control(g):
    bytestring = g.bytestring
    stack = g.stack
    i = g.i
    memory = g.memory
    labels = g.labels
    exit = g.exit

    control = bytestring[i:i+2]
    i += 2

    if control == '00':
        #set label at current location
        num, i = get_num(bytestring, i)
        labels[num] = i
    elif control == '01':
        #call subroutine
        num, i = get_num(bytestring, i)
        copyGlobals = Globals()
        g.copy_vals(copyGlobals)
        g.store(copyGlobals)
        g.i = i
    elif control == '02':
        #jump to label
        num, i = get_num(bytestring, i)
        i = labels[num]
    elif control == '10':
        #if top of stack 0, jump to label
        num, i = get_num(bytestring, i)
        if stack.pop() == 0:
            g.i = labels[num]
    elif control == '12':
        #if top of stack is negative, jump to label
        num, i = get_num(bytestring, i)
        if stack.pop() < 0:
            g.i = labels[num]
    elif control == '12':
        #end subroutine and pass control back to caller
        g.rollback()
    elif control == '22':
        #end program
        exit = True

    g.i = i
    g.labels = labels
    g.exit = exit


def io(g):
    i = g.i
    bytestring = g.bytestring
    stack = g.stack
    memory = g.memory
    control = bytestring[i:i+2]
    i += 2

    if control == '00':
        #output character at top of stack
        print(chr(stack.peek()), end='')
    elif control == '01':
        #output number at top of stack
        print(stack.peek(), end='')
    elif control == '10':
        #read character from input and store in addr of stack top value (not sure if pop or peek)
        char = ord(input())
        addr = stack.pop()
        memory[addr] = char
    elif control == '11':
        #read num from input and store in addr of stack top value (not sure if pop or peek)
        num = int(input())
        addr = stack.pop()
        memory[addr] = num

    g.i = i
    g.memory = memory


def get_num(bytestring, i):
    #working correctly
    num_string = ''
    ctr = 0
    if bytestring[i] == '1':
        mult = -1
    else:
        mult = 1

    i += 1
    for num in bytestring[i:]:
        ctr += 1
        if num == '2':
            if num_string:
                return (mult * int(num_string, 2)), i+ctr
            else:
                return 0, i+ctr

        num_string += num




