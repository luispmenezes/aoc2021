def solve(file_path):
    input_file = open(file_path, 'r')
    input_lines = input_file.readlines()

    vent_map = {}

    for line in input_lines:
        line_tokens = line.strip().split(' -> ')
        o_x = int(line_tokens[0].split(',')[0])
        o_y = int(line_tokens[0].split(',')[1])
        d_x = int(line_tokens[1].split(',')[0])
        d_y = int(line_tokens[1].split(',')[1])

        inc_x = -1 if o_x > d_x else 1
        inc_y = -1 if o_y > d_y else 1

        if o_x == d_x or o_y == d_y:
            for x in range(o_x, d_x + inc_x, inc_x):
                for y in range(o_y, d_y + inc_y, inc_y):
                    key = '{},{}'.format(x, y)
                    vent_map[key] = vent_map.get(key, 0) + 1

    return sum(value >= 2 for value in vent_map.values())


result = solve('input-test.txt')
print("Test Result: {}".format(result))
if result != 5:
    print("Failed Test")
    exit(0)
else:
    result = solve('input.txt')
    print("Result: {}".format(result))
