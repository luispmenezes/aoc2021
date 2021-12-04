def sum_unmarked(card):
    sum = 0
    for l in card:
        for c in l:
            if c >= 0:
                sum += c
    return sum


def draw_numbers(draw, cards):
    drawn = 1
    for d in draw:
        for i in range(len(cards)):
            cards[i] = [[n if n != d else -1 for n in ln] for ln in cards[i]]
            if drawn >= 5 and (-5 in map(sum, zip(*cards[i])) or -5 in [sum(y) for y in cards[i]]):
                return d, sum_unmarked(cards[i])
        drawn += 1


def build_card(lines):
    return [[int(n) for n in ln.split()] for ln in lines.rstrip("\n").split('\n')]


def solve(file_path):
    input_file = open(file_path, 'r')
    input_lines = input_file.readlines()

    lc = 0
    draw = []
    cards = []
    card_str = ''
    for line in input_lines:
        if lc == 0:
            draw = [int(n) for n in line.split(',')]
        elif lc > 1:
            if line == '\n':
                cards.append(build_card(card_str))
                card_str = ''
            else:
                card_str += line

        lc += 1
    if len(card_str) > 0:
        cards.append(build_card(card_str))

    last_draw, sum_unm = draw_numbers(draw, cards)

    return last_draw * sum_unm


result = solve('input-test.txt')
print("Test Result: {}".format(result))
if result != 4512:
    print("Failed Test")
    exit(0)
else:
    result = solve('input.txt')
    print("Result: {}".format(result))
