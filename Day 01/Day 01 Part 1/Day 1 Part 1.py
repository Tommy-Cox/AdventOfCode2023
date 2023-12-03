
"""
Defines where to find the Calibration Document
"""
file_path = '/Users/thomascox/Desktop/CalibrationDocument.txt'

def extract_calibration_value(line):
    """
    Extracts the calibration value from a line of text.
    The calibration value is formed by combining the first and last digits.
    """
    digits = [char for char in line if char.isdigit()]
    if not digits:
        return 0
    first_digit = digits[0]
    last_digit = digits[-1]
    return int(first_digit + last_digit)

def sum_calibration_values(file_path):
    """
    Reads the calibration document line by line, extracts calibration values from each line,
    and returns the sum of all these values.
    """
    total = 0
    with open(file_path, 'r') as file:
        for line in file:
            total += extract_calibration_value(line)
    return total

def main ():
    total_sum = sum_calibration_values(file_path)
    print(f"Total Sum of Calibration Values: {total_sum}")

if __name__ == "__main__":
    main()
