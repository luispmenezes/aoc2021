def solve(file_path):
    input_file = open(file_path, 'r')
    input_lines = input_file.readlines()

    bit_sums = []
    count = 0

    for line in input_lines:
        # print(line)
        char_idx = 0
        for char in line:
            if char.isnumeric():
                if char_idx > len(bit_sums) - 1:
                    bit_sums.append(int(char))
                else:
                    bit_sums[char_idx] += int(char)
                char_idx += 1
        count += 1
        # print(bit_sums)

    gamma_bin = ''
    epsilon_bin = ''

    for s in bit_sums:
        mcv = s // (count // 2)
        lcv = (mcv + 1) % 2
        gamma_bin += str(mcv)
        epsilon_bin += str(lcv)

    # print(gamma_bin)
    # print(epsilon_bin)

    gamma = int(gamma_bin, 2)
    epsilon = int(epsilon_bin, 2)

    return gamma, epsilon, gamma * epsilon


r_gamma, r_epsilon, result = solve('input-test.txt')
print("Test Result: {} (gamma: {}, epsi: {})".format(result, r_gamma, r_epsilon))
if result != 198:
    print("Failed Test")
    exit(0)
else:
    r_gamma, r_epsilon, result = solve('input.txt')
    print("Result: {} (gamma: {}, epsi: {})".format(result, r_gamma, r_epsilon))
