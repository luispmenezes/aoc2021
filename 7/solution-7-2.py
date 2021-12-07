from statistics import median, mean


def solve(file_path):
    input_file = open(file_path, 'r')
    input_lines = input_file.readlines()

    positions = []

    for line in input_lines:
        positions += [int(lt) for lt in line.strip().split(',')]

    mean_x = round(mean(positions))
    search_range = 2
    candidates = []

    for target in range(mean_x - search_range, mean_x + search_range):
        candidates.append(sum(abs(target - x) * (abs(target - x) + 1) / 2 for x in positions))

    return int(min(candidates))


result = solve('input-test.txt')
print("Test Result: {}".format(result))
if result != 168:
    print("Failed Test")
    exit(0)
else:
    result = solve('input.txt')
    print("Result: {}".format(result))
