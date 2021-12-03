
def find_final_horizontal_by_horizontal_depth(filename):
    aim = 0
    forward = 0
    depth = 0
    with open(filename, "rt") as f:
        num = None
        while line := f.readline():
            print(line, end="")
            num = int(line[len(line) - 2])
            if line[0] == "f":
                forward += num
                depth += aim * num
            elif line[0] == "u":
                aim -= num
            elif line[0] == "d":
                aim += num

    print("Forward: ", forward, " Down: ", down, " Up: ", up, " Aim: ", aim, " Depth: ", depth)
    print("Forward final * Depth final: ", forward * depth)


if __name__ == "__main__":
    find_final_horizontal_by_horizontal_depth("input.txt")
