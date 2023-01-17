def isCollinear(x1, y1, x2, y2, x3, y3):
    a = x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)

    if a == 0:
        return True
    else:
        return False


def consistent(arr, poz):
    return len(arr) - poz > 0


def solution(arr):
    return len(arr) > 2


def solution(inputArr, poz1, poz2, solArr):
    if len(solArr) == 0:
        solArr.append(inputArr.at(poz1))
        solArr.append(inputArr.at(poz2))
    elif len(solArr) == 1:
        solArr.append(inputArr.at(poz1))
    elif isCollinear():


