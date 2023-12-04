
def part1():
    total = 0
    with open("input") as file:
        for line in file:
            digits = [c for c in line if c.isnumeric()]
            total += int(digits[0] + digits[-1])
    print(total)

def part2():
    total = 0
    nums = {'zero': '0',
            'one': '1',
            'two': '2',
            'three': '3',
            'four': '4',
            'five': '5',
            'six': '6',
            'seven': '7',
            'eight': '8',
            'nine': '9'}
    with open("input") as file:
        for line in file:
            digits = []
            i = 0
            while i < len(line):
                if line[i].isdigit():
                    digits.append(line[i])
                else:
                    for alpha, num in nums.items():
                        if line.startswith(alpha, i):
                            digits.append(num)
                            break
                i += 1
            total += int(digits[0] + digits[-1])
    print(total)
    
part1()
part2()



'''
debugging notes

version of part2 using replace() fails for
qkneightwofourninejzjfmkjv8eightthdtp
(we replaced two before eight and missed the eight)

next version failed because we were greedily
getting nums from left to right and would thus
miss the rightmost word digit sometimes
(fixed by allowing overlaps)

'''