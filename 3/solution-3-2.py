from binarytree import Node


def solve(file_path):
    input_file = open(file_path, 'r')
    input_lines = input_file.readlines()

    root = Node(-1)

    for line in input_lines:
        curr_node = root
        for char in line:
            if char == '0':
                if curr_node.left is None:
                    curr_node.left = Node(1)
                else:
                    curr_node.left.value += 1
                curr_node = curr_node.left
            elif char == '1':
                if curr_node.right is None:
                    curr_node.right = Node(1)
                else:
                    curr_node.right.value += 1
                curr_node = curr_node.right
    print(root)

    # OXY
    oxy_str = ''

    n_o = root
    while n_o.left is not None or n_o.right is not None:
        if n_o.left is not None and (n_o.right is None or n_o.left.value > n_o.right.value):
            oxy_str += '0'
            n_o = n_o.left
        else:
            oxy_str += '1'
            n_o = n_o.right

    oxy = int(oxy_str, 2)

    # CO2
    co2_str = ''

    n_c = root
    while n_c.left is not None or n_c.right is not None:
        if n_c.left is not None and (n_c.right is None or n_c.left.value <= n_c.right.value):
            co2_str += '0'
            n_c = n_c.left
        else:
            co2_str += '1'
            n_c = n_c.right
    co2 = int(co2_str, 2)

    return oxy, co2, oxy * co2


r_gamma, r_epsilon, result = solve('input-test.txt')
print("Test Result: {} (gamma: {}, epsi: {})".format(result, r_gamma, r_epsilon))
if result != 230:
    print("Failed Test")
    exit(0)
else:
    r_gamma, r_epsilon, result = solve('input.txt')
    print("Result: {} (gamma: {}, epsi: {})".format(result, r_gamma, r_epsilon))
