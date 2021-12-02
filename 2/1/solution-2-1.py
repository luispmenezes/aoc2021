def solve(file_path):
    input_file = open(file_path, 'r')
    input_lines = input_file.readlines()

    x = 0
    y = 0

    for line in input_lines:
        action = line.split(' ')[0]
        delta = int(line.split(' ')[1])

        if action == 'forward':
            x += delta
        elif action == 'up':
            y -= delta
        elif action == 'down':
            y += delta

    return x, y, x * y


x, y, result = solve('input-test.txt')
print("Test Result: {}".format(result))
if result != 150:
    print("Failed Test")
    exit(0)
else:
    x, y, result = solve('input.txt')
    print("Result: {}".format(result))
