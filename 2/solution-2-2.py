def solve(file_path):
    input_file = open(file_path, 'r')
    input_lines = input_file.readlines()

    x = 0
    y = 0
    aim = 0

    for line in input_lines:
        action = line.split(' ')[0]
        delta = int(line.split(' ')[1])

        if action == 'forward':
            x += delta
            y += (aim * delta)
        elif action == 'up':
            aim -= delta
        elif action == 'down':
            aim += delta

    return x, y, x * y


r_x, r_y, result = solve('input-test.txt')
print("Test Result: {} ({},{})".format(result, r_x, r_y))
if result != 900:
    print("Failed Test")
    exit(0)
else:
    r_x, r_y, result = solve('input.txt')
    print("Result: {}".format(result))
