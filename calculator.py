"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


while True:
    def get_valid_input():
        commands = ["+", "-", "*", "/", "square", "pow", "mod", "cube"]
        input_string = input("> ")
        tokens = input_string.split()
        for i in range(1, len(tokens)):
            while True:
                try:
                    token = float(tokens[i])
                    if token: 
                        break
                except ValueError:
                    print("Please enter valid numbers!")
                    input_string = input("> ")
                    tokens = input_string.split()
        while True:
            if tokens[0] in commands: 
                    break
            else:
                print("Please enter a valid command!")
                input_string = input("> ")
                tokens = input_string.split()
        return tokens

    
    def get_floats(token0):
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
        elif token0 == 'square':
            token0 = square
        elif token0 == 'cube':
            token0 = cube
        return token0(tokens)

    
    tokens = get_valid_input()
    if tokens[0] == 'q':
        break
    else:
        print(get_floats(tokens[0]))
   
