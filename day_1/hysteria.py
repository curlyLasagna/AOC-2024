import types
l1: list[int] = []
l2: list[int] = []
with open("input.txt") as f:
    for line in f.readlines():
        l1.append(int(line.split()[0]))
        l2.append(int(line.split()[1]))

l1.sort()
l2.sort()
distance = 0
for i in range(len(l1)):
    distance += abs(l1[i] - l2[i])

print(distance)
