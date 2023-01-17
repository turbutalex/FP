from typing import no_type_check


def isPrime(n):
    if n==1 or n ==0 :
        return False
    if n==2:
        return True
    else:
        for d in range(2,int(n/2)):
            if n%d==0:
                return False
        return True
def nextPrime(n):
    if isPrime(n) == True:
        return n
    else:
        d=n
        while isPrime(d) == False:
            d = d+1
    return d


print(nextPrime(7))
