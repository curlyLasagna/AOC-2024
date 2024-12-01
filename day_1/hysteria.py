import types
from collections import Counter

def part_1():
    l1: list[int] = []
    l2: list[int] = []
    with open("input.txt") as f:
        for line in f.readlines():
            l1.append(int(line.split()[0]))
            l2.append(int(line.split()[1]))

    l1.sort()
    l2.sort()
    distance:int = 0
    for i in range(len(l1)):
        distance += abs(l1[i] - l2[i])

    print(distance)

def part_2():
    map1 = {}
    map2 = {}
    l1 = []
    l2 = []
    similarity_score:int = 0
    with open("input.txt") as f:
        for line in f.readlines():
            l1.append(int(line.split()[0]))
            l2.append(int(line.split()[1]))

    map1 = Counter(l1)
    map2 = Counter(l2)

    for e in map1:
        similarity_score += e * map1[e] * map2[e]

    print(similarity_score)

part_2()
