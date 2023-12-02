"""
Defines where to find the Calibration Document
"""

file_path = '/Users/thomascox/Desktop/CalibrationDocument.txt'

def extract_calibration_value(line):
    """
    Extracts the calibration value from a line of text.
    The calibration value is formed by combining the first and last digits,
    where digits can be numeric or spelled out (ex: 'one', 'two' OR '1', '2').
    """
    digit_map = {
        "one": "o1ne", 
        "two": "tw2o", 
        "three": "thr3ee", 
        "four": "fo4ur",
        "five": "fi5ve", 
        "six": "s6ix", 
        "seven": "sev7en", 
        "eight": "eig8ht", 
        "nine": "ni9ne"
    }
    for word, num in digit_map.items():
        line = line.replace(word, num)

    digits = [char for char in line if char.isdigit()]
    if not digits:
        return 0
    first_digit = digits[0]
    last_digit = digits[-1]
    return int(first_digit + last_digit)


def sum_calibration_values(file_path):
    """
    Reads a file line by line, extracts calibration values from each line,
    and returns the sum of all these values.
    """
    total = 0
    with open(file_path, 'r') as file:
        for line in file:
            total += extract_calibration_value(line)
    return total

def main():
    total_sum = sum_calibration_values(file_path)
    print(f"Total Sum of Calibration Values: {total_sum}")

if __name__ == "__main__":
    main()
