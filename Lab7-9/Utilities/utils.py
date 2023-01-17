from math import floor


def insertSort(l, *, key=lambda x: x, reverse=False):
    """
    sort the element of the list
    l - list of element
    return the ordered list (l[0]<l[1]<...)
    """
    for i in range(1, len(l)):
        ind = i - 1
        a = l[i]
        if not reverse:
            while ind >= 0 and key(a) < key(l[ind]):
                l[ind + 1] = l[ind]
                ind -= 1
        else:
            while ind >= 0 and key(a) > key(l[ind]):
                l[ind + 1] = l[ind]
                ind -= 1
        l[ind + 1] = a


def get_next_gap(gap):
    gap = (gap * 10) / 13
    if gap < 1:
        return 1
    return gap


def combSort(l, *, key=lambda x: x, reverse=False):
    gap = len(l)
    swapped = True
    while gap != 1 or swapped == True:
        gap = get_next_gap(gap)
        swapped = False
        for i in range(len(l) - gap):
            if not reverse:
                if key(l[i] > l[i + floor(gap)]):
                    swapped = True
                    l[i], l[i + floor(gap)] = l[i + floor(gap)], l[i]
            else:
                if key(l[i] < l[i + floor(gap)]):
                    swapped = True
                    l[i], l[i + floor(gap)] = l[i + floor(gap)], l[i]
