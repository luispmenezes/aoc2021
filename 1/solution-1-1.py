input_file = open('input.txt', 'r')
input_lines = input_file.readlines()

last_meas = None
increase_count = 0

for line in input_lines:
    cur_meas = int(line)
    if last_meas is None:
        print("{} (N/A - no previous measurement)".format(cur_meas))
    else:
        if cur_meas > last_meas:
            print("{} (increased)".format(cur_meas))
            increase_count += 1
        elif cur_meas < last_meas:
            print("{} (decreased)".format(cur_meas))
        else:
            print("{} (same)".format(cur_meas))
    last_meas = cur_meas

print("Time increased: {}".format(increase_count))
