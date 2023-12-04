
def is_part_num(input, row, col_start, col_end):
    rows = len(input)
    cols = len(input[0])
    todo = [(row-1, i) for i in range(col_start-1, col_end+1)] + \
            [(row+1, i) for i in range(col_start-1, col_end+1)] + \
            [(row, col_start-1), (row, col_end)]
    for r, c in todo:
        if r >= 0 and c >= 0 and r < rows and c < cols and \
            not input[r][c].isdigit() and input[r][c] != '.':
            return True
    return False

def part1():
    input = []
    with open("input") as file:
        for line in file:
            input.append(line.strip())

    total = 0
    for i, row in enumerate(input):
        left, right = 0, 0
        while left < len(row):
            if row[left].isdigit():
                right = left
                while right < len(row) and row[right].isdigit():
                    right += 1
                if is_part_num(input, i, left, right):
                    total += int(row[left:right])
                left = right
            left += 1
    print(total)


# ret 0 if not gear
def get_gear_ratio(input, r, c):
    todo = [(r-1, c-1), (r-1, c), (r-1, c+1), 
            (r, c-1), (r, c+1),
            (r+1, c-1), (r+1, c), (r+1, c+1)]
    nums = []
    skip = set()
    for row, col in todo:
        if (row, col) not in skip and input[row][col].isdigit():
            left, right = col, col 
            while left >= 0 and input[row][left].isdigit():
                if (row, left) in todo:
                    skip.add((row, left))
                left -= 1
            while right < len(input[row]) and input[row][right].isdigit():
                if (row, right) in todo:
                    skip.add((row, right))
                right += 1
            # print(input[row][left+1], input[row][right-1], input[row][left+1:right])
            nums.append(int(input[row][left+1:right]))
        
    # for row, col in todo:
    #     if input[row][col].isdigit():
    #         if (row, col-1) in nums or (row, col-2) in nums and input[row][col-1] != '.':
    #             continue
    #         nums.append((row, col))
    return 0 if len(nums) != 2 else nums[0] * nums[1]

def part2():
    input = []
    with open("input") as file:
        for line in file:
            input.append(line.strip())

    total = 0
    for i, row in enumerate(input):
        for j, elem in enumerate(row):
            if elem == '*':
                total += get_gear_ratio(input, i, j)
    print(total)


part1()
part2()


