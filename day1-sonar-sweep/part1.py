
def find_increasing_nums(filename):
    increases = 0
    with open(filename, "rt") as f:
        line = 0
        last_value = 0
        while line := f.readline():
            line = int(line)
            if line > last_value:
                increases += 1
            last_value = line
            print(line)

    f.close()
    print('total increases: ', increases-1)  # subtract one for the initial number


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    find_increasing_nums("input.txt")
