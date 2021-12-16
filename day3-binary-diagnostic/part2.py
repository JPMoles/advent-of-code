
def read_report_values(filename, reportValues):
    # Open file
    with open(filename) as f:
        while line := f.readline():
            reportValues.append(line[:-1])


def most_common_bit(reportValues, position):
    zeros = 0
    ones = 0
    for s in reportValues:
        if s[position] == '1':
            ones += 1
        else:
            zeros += 1

    return '1' if ones >= zeros else '0'


def least_common_bit(reportValues, position):
    zeros = 0
    ones = 0
    for s in reportValues:
        if s[position] == '1':
            ones += 1
        else:
            zeros += 1

    return '1' if zeros > ones else '0'


def find_oxygen_generator_rating(oxygenValues):
    pos = 0
    while len(oxygenValues) > 1:
        mcb = most_common_bit(oxygenValues, pos)
        print("for pos ", pos, " mcb is ", mcb)
        for s in oxygenValues.copy():
            if len(oxygenValues) == 1:
                break
            elif s[pos] != mcb:
                oxygenValues.remove(s)
        pos += 1
        print(oxygenValues)

    return oxygenValues[0]


def find_co2_scrubber_rating(co2Values):
    pos = 0
    while len(co2Values) > 1:
        lcb = least_common_bit(co2Values, pos)
        print(co2Values)
        print("for pos ", pos, " lcb is ", lcb)
        for s in co2Values.copy():
            if len(co2Values) == 1:
                break
            elif s[pos] != lcb:
                co2Values.remove(s)
        pos += 1

    return co2Values[0]


if __name__ == "__main__":
    reportValues = []
    read_report_values("input.txt", reportValues)

    oxygenValues = reportValues.copy()
    co2Values = reportValues.copy()

    print(reportValues)

    oxygen_rating_binary = find_oxygen_generator_rating(oxygenValues)
    co2_rating_binary = find_co2_scrubber_rating(co2Values)

    print("Oxygen rating in binary:", oxygen_rating_binary, " C02 rating in binary:", co2_rating_binary)
    oxygen_rating = int(oxygen_rating_binary, 2)
    co2_rating = int(co2_rating_binary, 2)
    print("Oxygen rating in decimal:", oxygen_rating, " C02 rating in binary:", co2_rating)
    print("Life support rating: ", oxygen_rating * co2_rating)
