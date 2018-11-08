from classtest2 import *

class testClass:
    val1 = 0
    val2 = 0
    def __init__(self):
        pass


def main():
    cl = testClass()
    testfxn(cl)
    print('Values in file 1:')
    print(cl.val1)
    print(cl.val2)


main()
