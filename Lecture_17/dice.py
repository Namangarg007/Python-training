def dice(processed, target, faces):
    if target == 0:
        print(processed)
        return

    for face in range(1, faces + 1):
        if face > target:
            continue

        dice(processed + str(face), target - face, faces)


print(dice("", 5, 3))


def dicepath3(processed, target, faces):
    if target == 0:
        if len(processed) <= 3:
            print(processed)
        return

    for face in range(1, faces + 1):
        if face > target:
            continue

        dicepath3(processed + str(face), target - face, faces)


print(dicepath3("", 5, 3))


def count_dice(processed, target, faces):
    if target == 0:
        return 1

    acc = 0
    for face in range(1, faces + 1):
        if face > target:
            continue

        acc += count_dice(processed + str(face), target - face, faces)
    return acc


print(count_dice("", 5, 3))
