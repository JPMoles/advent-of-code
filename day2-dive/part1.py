
def find_final_horizontal_and_depth(filename):
    forward = 0
    down = 0
    up = 0
    with open(filename, "rt") as f:
        line = None
        while line := f.readline():
            print(line, end="")
            if line[0] == "f":
                forward += int(line[len(line)-2])
            elif line[0] == "u":
                up += int(line[len(line)-2])
            elif line[0] == "d":
                down += int(line[len(line)-2])

    print("Forward: ", forward, " Down: ", down, " Up: ", up)
    depth = (down - up) if (down > up) else (up - down)
    print("Forward total: ", forward, " Depth total: ", depth)
    print("Forward total * Depth total: ", forward * depth)


if __name__ == "__main__":
    find_final_horizontal_and_depth("input.txt")