import math
def calculate_factorials(input_file, output_file):
    try:
        with open(input_file, 'r') as f_in, open(output_file, 'w') as f_out:
            for line in f_in:
                try:
                    num = int(line.strip())
                    if num < 0:
                        f_out.write(f"Error: Factorial not defined for negative numbers: {num}\n")
                    else:
                        factorial = math.factorial(num)
                        f_out.write(f"{num}! = {factorial}\n")
                except ValueError:
                    f_out.write(f"Error: Invalid input - not an integer: {line.strip()}\n")
    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")

# Usage
input_file = 'input.txt'
output_file = 'output.txt'
calculate_factorials(input_file, output_file)