with open('input.txt') as f:
    content = f.read()
array = content.split()
numbers = list(map(int, array))

larger = 0
for i in range(1, len(numbers)):
    if numbers[i] > numbers[i-1]:
        larger = larger + 1
print(larger)
