input_file = open('input.txt', 'r')
input_lines = input_file.readlines()

last_three_meas = []
increase_count = 0

for line in input_lines:
    cur_meas = int(line)

    if len(last_three_meas) < 3:
        print("{} (N/A - no previous sum) - ".format(cur_meas) + ' '.join([str(m) for m in last_three_meas]))
    else:
        last_window = sum(last_three_meas)
        curr_window = sum(last_three_meas[1:]) + cur_meas

        if curr_window > last_window:
            print("{} (increased) - ".format(cur_meas) + ' '.join([str(m) for m in last_three_meas]))
            increase_count += 1
        elif curr_window < last_window:
            print("{} (decreased) - ".format(cur_meas) + ' '.join([str(m) for m in last_three_meas]))
        else:
            print("{} (no change) - ".format(cur_meas) + ' '.join([str(m) for m in last_three_meas]))

    if len(last_three_meas) == 3:
        last_three_meas.pop(0)
    last_three_meas.append(cur_meas)

print("Time increased: {}".format(increase_count))
