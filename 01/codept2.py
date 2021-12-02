with open('input.txt') as f:
    content = f.read()
array = content.split()
numbers = list(map(int, array))

larger = 0
previous = 0

# This returns the "correct" answer, but clearly counts the first 3-window, so I'm not
# sure what's going on with either me or AOC. Blame the weed.
for i in range(2, len(numbers)-1):
    val = numbers[i] + numbers[i-1] + numbers[i-2]
    if val > previous:
        larger = larger + 1
    previous = val
print(larger)