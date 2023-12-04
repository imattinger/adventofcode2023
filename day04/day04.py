

def part1():
    score = 0
    with open("input") as file:
        for line in file:
            card = line.split(': ')[1].split()
            winners = set(card[:10])
            scratch = set(card[11:])
            # possible bug if we get duplicate winning numbers
            matches = len(scratch.intersection(winners))
            if matches > 0:
                score += 2 ** (matches - 1)
    print(score)

def part2():
    scores = {}
    with open("input") as file:
        for i, line in enumerate(file):
            card = line.split(': ')[1].split()
            winners = set(card[:10])
            scratch = set(card[11:])
            scores[i] = len(scratch.intersection(winners))
    total_cards = 0
    card_counts = [1] * len(scores)
    for i, count in enumerate(card_counts):
        total_cards += count
        for j in range(1, scores[i] + 1):
            if i + j < len(card_counts):
                card_counts[i + j] += count
    print(total_cards)
        

part1()
part2()

'''

bug from 
    card = line.strip().split(': ')[1].split(' ')
    ...
    winners = set(card[:10])

where card now contains a bunch of '' 
so card[:10] didn't necessarily include all ten winners 

passing no arg to split() makes it treat whitespace runs as 
a single separator

also note there's no need for the strip() if we're doing that

'''
