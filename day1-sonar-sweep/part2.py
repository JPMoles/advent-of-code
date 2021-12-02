
def find_increasing_windows(filename):
    increases = 0
    with open(filename, "rt") as f:
        rolling_window = [int(f.readline()), int(f.readline()), int(f.readline())]
        last_num = 0  # index in rolling_window
        window_sum = sum(rolling_window, 0)  # initial window

        while line := f.readline():
            line = int(line)  # new number
            # print("Num: ", line)
            prev_window = window_sum
            # print("Prev window: ", prev_window)
            window_sum = (window_sum + line) - rolling_window[last_num % 3]
            # print("New window: ", window_sum)
            rolling_window[last_num % 3] = line  # replace value at last_num
            # print("Updated rolling window: ", rolling_window)

            if window_sum > prev_window:
                increases += 1

            # print("Is window_sum (", window_sum, ") > ", prev_window, " prev_window: ", window_sum > prev_window)
            # print("Increases: ", increases)

            last_num += 1  # increment rolling location in array
            # print("New location in array: ", last_num % 3, end="\n\n")

    f.close()
    # print('total increases: ', increases)  # no need to subtract one because started at sliding-window 1


if __name__ == "__main__":
    find_increasing_windows("input.txt")