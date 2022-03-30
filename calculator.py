"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


while True:
    input_string = input("> ")
    tokens = input_string.split()

    def get_floats(token0, token1, token2):
        if token0 == 'pow':
            token0 = power
        elif token0 == '+':
            token0 = add
        elif token0 == '-':
            token0 = subtract
        elif token0 == '*':
            token0 = multiply
        elif token0 == '/':
            token0 = divide
        elif token0 == 'mod':
            token0 = mod
        return token0(float(token1), float(token2))

    if tokens[0] == 'q':
        break
    elif tokens[0] == 'square':
        print(square(float(tokens[1])))
    elif tokens[0] == 'cube':
        print(cube(float(tokens[1])))
    else:
        print(get_floats(tokens[0], tokens[1], tokens[2]))
   

