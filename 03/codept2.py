from numpy import array, transpose, bincount



with open('input.txt') as f:
    oxygen = [list(map(int, list(val))) for val in f.read().split("\n")]
    co2 = oxygen.copy()
    for i in range(0, 12):
        if(len(oxygen) > 1):
            transpose_oxy = transpose(oxygen)
            bincount_oxy = array([bincount(elem) for elem in transpose_oxy])
            if(bincount_oxy[i][0] > bincount_oxy[i][1]):
                oxygen = list(filter(lambda reading: reading[i] == 0 , oxygen))
            else:
                oxygen = list(filter(lambda reading: reading[i] == 1 , oxygen))

        if(len(co2) > 1):
            transpose_co2 = transpose(co2)
            bincount_co2 = array([bincount(elem) for elem in transpose_co2])
            if(bincount_co2[i][0] > bincount_co2[i][1]):
                co2 = list(filter(lambda reading: reading[i] == 1 , co2))
            else:
                co2 = list(filter(lambda reading: reading[i] == 0 , co2))
    print(int("".join(str(i) for i in oxygen[0]),2) * int("".join(str(i) for i in co2[0]),2))
    

