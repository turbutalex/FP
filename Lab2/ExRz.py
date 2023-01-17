def isPrime(n):
    if n==1 or n ==0 :
        return False
    if n==2:
        return True
    else:
        for d in range(2,int(n/2)+1):
            if n%d==0:
                return False
        return True
def nSequence(n):
    if n==0:
        return 0
    if n==1 or n==2 or n==3:
        return n
    c=4
    pos=3
    nr=2
    while pos<n:
        if isPrime(c) == True:
            pos = pos+1
            nr=c
        else:
            for i in range(2,int(c/2)+1):
                if c%i==0 and isPrime(i) == True:
                    pos=pos+i
                    nr=i
                if pos>=n:
                    return nr              
        c=c+1
                
    return nr

for i in range(1,100):
    print(nSequence(12))


