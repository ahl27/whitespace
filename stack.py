#quick implementation of a stack

class Stack:
    def __init__(self):
        self.stack_arr = []

    def push(self, obj):
        self.stack_arr.append(obj)

    def pop(self):
        ret_val = self.stack_arr[-1]
        self.stack_arr = self.stack_arr[:-1]
        return ret_val

    def peek(self):
        return self.stack_arr[-1]

    def get_item(self, index):
        return self.stack_arr[-index]

    def is_empty(self):
        if len(self.stack_arr) is not 0:
            return False
        else:
            return True