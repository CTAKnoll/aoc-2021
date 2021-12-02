with open('input.txt') as f:
    content = f.read()
array = content.split()
numbers = list(map(int, array))

larger = 0
previous = 0

for i in range(2, len(numbers)):
    val = numbers[i] + numbers[i-1] + numbers[i-2]
    if val > previous and i != 2:
        larger = larger + 1
    previous = val
print(larger)