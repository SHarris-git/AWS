## GSH 7/24/24 
## This code prints "Hello, World!" and sums 2 numbers provided by user
##
## To run this code use this cmd: hello2.py <number> <number>
##

import sys

print('Hello, World!')

if len(sys.argv) < 3:
    print('Please provide two numbers as arguments.')
    sys.exit(1)

try:
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])
    result = num1 + num2
    print(f'The sum of {num1} and {num2} is {result}.')
except ValueError:
    print('Please provide valid integer arguments.')
    sys.exit(1)