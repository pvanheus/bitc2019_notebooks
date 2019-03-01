import sys

def arith(operation, num1, num2):
    """arith: do some arithmetic

    operation: either 'add' or 'subtract'
    num1: first number - int
    num2: second number for operation - int"""
    if operation == 'add':
        print(num1 + num2)
    elif operation == 'subtract':
        print(num1 - num2)
    else:
        print('unknown operation:', operation)

if __name__ == '__main__':
    script = sys.argv[0]
    if len(sys.argv) != 4:
        print("Arithmetic script")
        print("Usage: " + script + " <operation> <num1> <num2>")
        print("where <operation> is add or subtract and <num1> and <num2> are integers")
        sys.exit(1)

    operation = sys.argv[1]
    try:
        num1 = int(sys.argv[2])
    except ValueError as e:
        print("num1 should be a number:", str(e))
    try:
        num2 = int(sys.argv[3])
    except ValueError as e:
        print("num2 should be a number:", str(e))
    arith(operation, num1, num2)
