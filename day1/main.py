with open("day1_input.txt") as f:
    groups = f.read().split("\n\n")

sum_per_group = []

for _ in range(len(groups)):
    sum_per_group.append(sum(map(int, groups[_].split("\n"))))

print("Day 1 | Part 1:", max(sum_per_group))
print("Day 1 | Part 2:", sum(sorted(sum_per_group, reverse=True)[:3]))
