import string

with open("input_data.txt", "r") as file:
    data = file.readlines()

alphabet = list(string.ascii_letters)

union = []

for item in data:
    item = item.split("\n")[0]

    first = item[: len(item) // 2]
    second = item[len(item) // 2 :]

    intersection = set(first).intersection(second)

    for _ in intersection:
        union.append(alphabet.index(_) + 1)
