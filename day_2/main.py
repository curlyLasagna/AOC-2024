listy = []
safe:int = 0

with open("./inputs.txt") as f:

    for line in f.readlines():
        isSafe: bool = True
        listy = list(map(int, line.split(' ')))
        diff_list = []
        for i in range(1, len(listy)):
             diff_list.append(listy[i - 1] - listy[i])

        # Increasing
        # Check if all values in the diff_list are negative
        if diff_list[0] < 0:
            for e in diff_list:
                # Running into an unsafe value
                if e >= 0:
                    isSafe = False
                    continue
                # Check if increasing interval is between 1, 2 or 3
                elif not (1 <= abs(e) <= 3):
                    isSafe = False
                    continue


        # Decreasing
        else:
            for e in diff_list:
                if e <= 0:
                    isSafe = False
                    continue
                elif not (1 <= abs(e) <= 3):
                    isSafe = False
                    continue


        if isSafe:
            safe += 1
print(safe)
