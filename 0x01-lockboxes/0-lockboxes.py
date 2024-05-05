# !/usr/bin/python3
""" Lock Boxes """


def canUnlockAll(boxes):
    """ Lock Boxes """
    for ind in range(1, len(boxes)):
        check = False
        for box in range(len(boxes)):
            if ind in boxes[box] and ind != box:
                check = True
        if not check:
            return False
    return True
