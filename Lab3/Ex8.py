#Returns the longest sequence that is made up of numbers in the interval [0,10]
def p8(n,l):
    seq = []
    error = "No available sequence"
    if len(l)>=1:
        k=0
        startPos = 0
        max=0
        for i in range(0,n):
            if l[i] >=0 and l[i]<=10:
                k = k + 1
            else:
                k = 0
            if k>max:
                max = k
                startPos = i - k + 1  
        i=startPos
        while i<startPos+max:
            seq.append(int(l[i]))
            i = i+1
        if len(seq)>0:
            return seq
        else:
            return error
            
    else:
        return error
        



