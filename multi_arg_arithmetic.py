# example command line
# python3 multi_arg_arithmetic.py add 1 2 3 4 5
import sys

if len(sys.argv) < 4:
    print('error')
    sys.exit(1)

operation = sys.argv[1]

numbers = []
for parameter in sys.argv[2:]:
    numbers.append(int(parameter))

if operation == 'add':
    total = sum(numbers)
    print('add', total)
elif operation == 'subtract':
    total = numbers[0]
    for num in numbers[1:]:
        total = total - num
    print('subtract', total)
elif operation == 'multiply':
    total = numbers[0]
    for num in numbers[1:]:
        total = total * num
    print('multiply', total)
elif operation == 'divide':
    total = numbers[0]
    for num in numbers[1:]:
        try:
            total = total / num
        except ZeroDivisionError:
            print('cannot divide by zero')
            sys.exit(1)
    print('divide', total)
else:
    print('unknown operation')
    sys.exit(1)
