import re

cubes = {"red": 12, "green": 13, "blue": 14}

def validate_game(game):
    a = re.split(': |; |, ', game)
    for i in range(1, len(a)):
        b = re.split(' ', a[i])
        if int(b[0]) > cubes[b[1]]:
            return 0
    return int(re.split(' ', a[0])[1])

def part1():
    total = 0
    with open("input") as file:
        for line in file:
            total += validate_game(line.strip())
    print(total)

def part2():
    total = 0
    with open("input") as file:
        for game in file:
            handfuls = re.split(': |; |, ', game.strip())[1:]
            red, green, blue = 0, 0, 0
            for handful in handfuls:
                b = re.split(' ', handful)
                if b[1] == 'red':
                    red = max(red, int(b[0]))
                elif b[1] == 'green':
                    green = max(green, int(b[0]))
                elif b[1] == 'blue':
                    blue = max(blue, int(b[0]))
            total += red * green * blue
    print(total)

part1()
part2()
