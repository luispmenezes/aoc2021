def solve(file_path):
    input_file = open(file_path, 'r')
    input_lines = input_file.readlines()

    state = []

    for line in input_lines:
        state += [int(d) for d in line.strip().split(',')]

    print('Initial state: {}'.format(','.join([str(s) for s in state])))

    for d in range(80):
        for i in range(len(state)):

            if state[i] == 0:
                state[i] = 6
                state.append(8)
            else:
                state[i] -= 1

        print('After {} day: {}'.format(d, ','.join([str(s) for s in state])))

    return len(state)


result = solve('input-test.txt')
print("Test Result: {}".format(result))
if result != 5934:
    print("Failed Test")
    exit(0)
else:
    result = solve('input.txt')
    print("Result: {}".format(result))
