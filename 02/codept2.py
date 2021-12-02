coord = [0,0,0]

def parse(str):
    arr = str.split(" ")
    if(arr[0] == "forward"):
        coord[0] = coord[0] + int(arr[1])
        coord[1] = coord[1] + int(arr[1]) * coord[2]
    if(arr[0] == "up"):
        coord[2] = coord[2] - int(arr[1])
    if(arr[0] == "down"):
        coord[2] = coord[2] + int(arr[1])

with open('input.txt') as f:
    content = f.read()
    for str in content.split("\n"):
        print(str)
        parse(str)
print(coord[0] * coord[1])


