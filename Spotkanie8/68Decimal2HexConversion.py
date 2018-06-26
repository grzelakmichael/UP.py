# Convert a decimal to a hex as a string
def decimal_to_hex(decimal_value):
    hex_string = " "
    while decimal_value != 0:
        hex_value = decimal_value % 16
        hex_string = to_hex_char(hex_value) + hex_string
        decimal_value = decimal_value // 16
    return hex_string

    # Convert an integer to a single hex_string digit as a character


def to_hex_char(hex_value):
    if 0 <= hex_value <= 9:
        return chr(hex_value + ord('0'))

    else:  # 10 <= hexValue <= 15
        return chr(hex_value - 10 + ord('A'))


def main():
    # Prompt the user to enter a decimal integer
    decimal_value = eval(input("Enter a decimal number: "))
    print("The hex number for decimal", decimal_value, "is", decimal_to_hex(decimal_value))
