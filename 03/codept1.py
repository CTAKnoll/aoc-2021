from numpy import array, transpose, bincount

with open('input.txt') as f:
    content = [list(map(int, list(val))) for val in f.read().split("\n")]
    content = transpose(content)
    bincounts = array([bincount(elem) for elem in content])
    gamma = ""
    epsilon = ""
    for by_bit_count in bincounts:
        if(by_bit_count[0] >= by_bit_count[1]):
            gamma = gamma + "0"
            epsilon = epsilon + "1"
        else:
            gamma = gamma + "1"
            epsilon = epsilon + "0"
    gamma = int(gamma, 2)
    epsilon = int(epsilon, 2)
    print(gamma * epsilon)

