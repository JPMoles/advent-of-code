
def find_power_consumption(filename):
    with open(filename, "rt") as f:
        nums = [0] * 12  # increment or decrement by 1
        g_final_num = [""] * 12
        while line := f.readline():
            print(line, end="")
            for i in range(0, len(line)-1):
                if line[i] == "1":
                    nums[i] = nums[i] + 1
                else:
                    nums[i] = nums[i] - 1

        for i in range(0, len(nums)):
            if nums[i] > 0:
                g_final_num[i] = "1"
            else:
                g_final_num[i] = "0"

        gamma = int(''.join(g_final_num), 2)
        print("Final number (in binary): ", g_final_num, " Decimal (gamma): ", gamma)

        # don't know how to use ~ operator in python to operate on bits so here's a for loop instead
        e_final_num = ""
        for letter in g_final_num:
            if letter == "1":
                e_final_num += "0"
            else:
                e_final_num += "1"

        epsilon = int(''.join(e_final_num), 2)
        print("Epsilon in binary: ", e_final_num, " Decimal (epsilon): ", epsilon)

        print("Gamma * Epsilon: ", gamma * epsilon)


if __name__ == "__main__":
    find_power_consumption("input.txt")