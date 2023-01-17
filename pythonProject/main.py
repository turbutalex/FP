def partition(l, left, right):
    pivot = l[left]
    i = left
    j = right
    while i != j:
        while l[j] >= pivot and i != j:
            j -= 1
        l[i] = l[j]
        while l[i] <= pivot and i != j:
            i += 1
        l[j] = l[i]
    l[i] = pivot
    return i


def quickSortRec(l, left, right):
    pos = partition(l, left, right)
    if left < pos - 1:
        quickSortRec(l, left, pos - 1)
    if right > pos + 1:
        quickSortRec(l, pos + 1, right)


def mergeSort(l):
    if len(l) > 1:
        mid = len(l) // 2
        left = l[:mid]
        right = l[mid:]

        mergeSort(left)
        mergeSort(right)

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                l[k] = left[i]
                i += 1
            else:
                l[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            l[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            l[k] = right[j]
            j += 1
            k += 1


def insertionSort(l):
    for i in range(1, len(l)):
        nr = i - 1
        a = l[i]
        while a <= l[nr] and nr >= 0:
            l[nr + 1] = l[nr]
            nr -= 1
        l[nr + 1] = a


def selectionSortDirect(l):
    for i in range(0, len(l) - 1):
        for j in range(i + 1, len(l)):
            if l[i] > l[j]:
                l[i], l[j] = l[j], l[i]


def selectionSort(l):
    for i in range(0, len(l) - 1):
        ind = i
        for j in range(i + 1, len(l)):
            if l[j] < l[ind]:
                ind = j
        if (i < ind):
            aux = l[i]
            l[i] = l[ind]
            l[ind] = aux


v = [3, 6, 1, 7, 3, 2, 9, 23]
# quickSortRec(v, 0, len(v) - 1)
# quickSort(v)
# mergeSort(v)
# insertionSort(v)
# selectionSortDirect(v)
# selectionSort(v)
print(v)
