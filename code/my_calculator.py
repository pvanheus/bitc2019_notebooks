import sys

def arithmetic():
    if len(sys.argv) == 4:  # check that we have the correct number of parameters 
        script = sys.argv[0]
        operation = sys.argv[1]
        num1 = sys.argv[2]
        num2 = sys.argv[3]
        if operation == 'add':
            try:
                print(num1, "+", num2, "=", int(num1) + int(num2))
            except ValueError as e:
                print("only floats and integers are permitted:", str(e))
            
            