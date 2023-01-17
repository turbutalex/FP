def partial_positive_sum(poz, a):
    if poz == len(a):
        return 0
    s = 0
    for index in range(poz, len(a)):
        if a[index] > 0:
            s += a[index]
        else:
            s -= a[index]
    return s


def suma(a):
    s = 0
    for index in range(0, len(a)):
        s += a[index]
    return s


def consistent(x, a):
    return suma(x) + partial_positive_sum(len(x), a) >= 0


def solution(x, a):
    return len(x) == len(a) and suma(x) >= 0


def solution_found(x):
    print(x)


def solve(x, a):
    for el in a:
        x.append(el)
        if consistent(x, a):
            if solution(x, a):
                solution_found(x)
        else:
            x[-1] *= -1
    if consistent(x, a):
        if solution(x, a):
            solution_found(x)


def back_rec(x, a, i, p, k=1):
    x.append(a[i] * k)
    if k == 1:
        p[i] = 1
    else:
        p[i] = 2
    if suma(p) == 2 * len(a):
        return
    if solution(x, a):
        solution_found(x)
    if not consistent(x, a):
        if p[i] != 2 and i > 0:
            x.pop()
            back_rec(x, a, i, p, -1)
        elif i == 0:
            return
        else:
            while p[i] == 2:
                p[i] = 0
                i -= 1
                x.pop()
            if len(x):
                x.pop()
                back_rec(x, a, i, p, -1)
            elif i == 0 and p[i] == 1:
                back_rec(x, a, i, p, -1)
            else:
                return
    if i == len(a) - 1:
        while p[i] == 2:
            p[i] = 0
            i -= 1
            x.pop()
        if len(x):
            x.pop()
            back_rec(x, a, i, p, -1)
        elif i == 0 and p[i] != 1:
            back_rec(x, a, i, p, -1)
        else:
            return
    else:
        back_rec(x, a, i + 1, p)


def back_it(x, a, p):
    k = 1
    i = 0
    while suma(p) < len(a) * 2:
        x.append(a[i] * k)
        if solution(x, a):
            solution_found(x)
            pass
        if k == 1:
            p[i] = 1
        else:
            p[i] = 2
        if suma(p) == len(a) * 2:
            return
        k = 1
        if i == len(a) - 1:
            while p[i] == 2:
                p[i] = 0
                i -= 1
                x.pop()
            x.pop()
            k = -1
        else:
            i += 1


v = [1, 3, 4, 7]
rez = []
used = []
for _ in range(len(v)):
    used.append(0)
back_rec(rez, v, 0, used)
# backIt(rez, v, used)

"""if not consistent(x, a):
            if p[i] != 2 and i > 0:
                x.pop()
                i -= 1
                k = -1
            else:
                while p[i] == 2:
                    p[i] = 0
                    i -= 1
                    x.pop()
                    k = -1
                if len(x):
                    i=-1
                    x.pop()
                    k =-1
            """
