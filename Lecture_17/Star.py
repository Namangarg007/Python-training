def starDown(row):
    if row == 0:
        return

    for i in range(row):
        print("*", end=" ")

    print()

    starDown(row - 1)


starDown(5)


def starUp(row):
    if row == 0:
        return

    starUp(row - 1)

    for i in range(row):
        print("*", end=" ")

    print()


starUp(5)


def starDownRec(row, col=0):
    if row == 0:
        return

    if col == row:
        print()
        starDownRec(row - 1, 0)
        return

    print("*", end=" ")
    starDownRec(row, col + 1)


starDownRec(5)
