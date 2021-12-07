from statistics import median


def solve(file_path):
    input_file = open(file_path, 'r')
    input_lines = input_file.readlines()

    x = []

    for line in input_lines:
        x += [int(lt) for lt in line.strip().split(',')]

    target_x = median(x)
    fuel = 0

    for xi in x:
        fuel += abs(xi - target_x)

    return fuel


result = solve('input-test.txt')
print("Test Result: {}".format(result))
if result != 37:
    print("Failed Test")
    exit(0)
else:
    result = solve('input.txt')
    print("Result: {}".format(result))
