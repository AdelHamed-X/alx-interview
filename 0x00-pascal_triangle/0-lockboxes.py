""" Lock Boxes """


def canUnlockAll(boxes):
    for ind in range(1, len(boxes) - 1):
        flat_list = [
            y
            for index in range(len(boxes))
            for y in boxes[index]
            if index != ind
        ]

        if ind not in flat_list:
            return False

    return True
