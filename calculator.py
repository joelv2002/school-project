import sys

def addition(x,y):
    return x + y

def subtraction(x,y):
    return x - y

def multiplication(x,y):
    return x * y

def dec_division(x,y):
    return float(x)/y

def int_division(x,y):
    return x // y

def indices(x,y):
    return x ** y

if __name__ == '__main__':
    args = sys.argv[1:]
    if args[0] == "addition":
        print(addition(int(args[1]),int(args[2])))
    if args[0] == "subtraction":
        print(subtraction(int(args[1]),int(args[2])))
    if args[0] == "multiplication":
        print(multiplication(int(args[1]),int(args[2])))
    if args[0] == "dec_division":
        print(dec_division(int(args[1]),int(args[2])))
    if args[0] == "int_division":
        print(int_division(int(args[1]),int(args[2])))
    if args[0] == "indices":
        print(indices(int(args[1]),int(args[2])))
