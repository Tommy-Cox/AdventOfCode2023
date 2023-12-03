import re

red_max = 12
green_max = 13
blue_max = 14
file_path= '/Users/thomascox/Desktop/Day2Input.txt'

def read_game_data(file_path):
    with open(file_path) as f:
        return f.read().split('\n')
        
def get_numbers(x):
    red_number = re.findall(r'[0-9]+ red', x)
    green_number = re.findall(r'[0-9]+ green', x)
    blue_number = re.findall(r'[0-9]+ blue', x)
    return red_number, green_number, blue_number

def get_digit(x, color):
    if color in ["red", "green", "blue"]:
        return re.findall(r'[0-9]+', x)
    return 0

games = read_game_data(file_path)

part1_answer = 0
for index, game in enumerate(games):
    sets = get_numbers(game)
    check = 0
    for red in sets[0]:
        if int(get_digit(red, "red")[0]) > red_max:
            check += 1
    for green in sets[1]:
        if int(get_digit(green, "green")[0]) > green_max:
            check += 1
    for blue in sets[2]:
        if int(get_digit(blue, "blue")[0]) > blue_max:
            check += 1
    if check == 0:
        part1_answer += index + 1

part2_answer = 0
for game in games:
    sets = get_numbers(game)
    red_min, green_min, blue_min = 0, 0, 0
    for red in sets[0]:
        red_check = int(get_digit(red, "red")[0])
        red_min = max(red_min, red_check)
    for green in sets[1]:
        green_check = int(get_digit(green, "green")[0])
        green_min = max(green_min, green_check)
    for blue in sets[2]:
        blue_check = int(get_digit(blue, "blue")[0])
        blue_min = max(blue_min, blue_check)
    part2_answer += red_min * green_min * blue_min

print("Part 1 answer:", part1_answer)
print("Part 2 answer:", part2_answer)
