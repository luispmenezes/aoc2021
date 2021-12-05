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

        inc_y = int((d_y - o_y) / (abs(d_y - o_y) if abs(d_y - o_y) > 0 else 1))
        inc_x = int((d_x - o_x) / (abs(d_x - o_x) if abs(d_x - o_x) > 0 else 1))

        x = o_x
        y = o_y

        while x != d_x or y != d_y:
            key = '{},{}'.format(x, y)
            vent_map[key] = vent_map.get(key, 0) + 1

            x += inc_x
            y += inc_y

        key = '{},{}'.format(d_x, d_y)
        vent_map[key] = vent_map.get(key, 0) + 1

    return sum(value >= 2 for value in vent_map.values())


result = solve('input-test.txt')
print("Test Result: {}".format(result))
if result != 12:
    print("Failed Test")
    exit(0)
else:
    result = solve('input.txt')
    print("Result: {}".format(result))
