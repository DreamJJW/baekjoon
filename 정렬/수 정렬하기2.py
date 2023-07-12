def countingValleys(steps, path):
    hike = 0
    height = 0
    path = list(path)
    for i in range(steps):
        if path[i] == 'D':
            if height == 0:
                hike += 1
            height -= 1
        elif path[i] == 'U':
            height += 1

    return hike

countingValleys(steps=10, path="UDUUUDUDDD")


