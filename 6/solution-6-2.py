def solve(file_path):
    input_file = open(file_path, 'r')
    input_lines = input_file.readlines()

    state = {}

    for line in input_lines:
        for s in [int(d) for d in line.strip().split(',')]:
            state[s] = state.get(s, 0) + 1

    for d in range(256):
        new_state = {}
        for s in sorted(state):
            if s == 0:
                new_state[6] = new_state.get(6, 0) + state[s]
                new_state[8] = new_state.get(8, 0) + state[s]
            else:
                new_state[s-1] = new_state.get(s-1, 0) + state[s]
        state = new_state

    return sum(state.values())


result = solve('input-test.txt')
print("Test Result: {}".format(result))
if result != 26984457539:
    print("Failed Test")
    exit(0)
else:
    result = solve('input.txt')
    print("Result: {}".format(result))
