#Returns the longest sequence of numbers where every in every 3 numbers 2 are identical 
# or 
# a sequence of 2 numbers if there is no sequence to match the first criteria
def p9(n,l):
    seq=[]
    error = "No available sequence"
    if len(l)>=2:
        value1 = l[0]
        value2 = l[1]
        k=2
        max=2
        startPos = 0
        for i in range(2,n):
            if l[i] == value1 or l[i] == value2 or value1 == value2:
                value1 = l[i-1]
                value2 = l[i]
                k = k+1
                if k>max:
                    max = k
                    startPos = i - k + 1

            else:
                value1 = l[i-1]
                value2 = l[i]
                k=2
        i =startPos
        while i<startPos+max:
            seq.append(int(l[i]))
            i = i+1
        if len(seq)>0:
            return seq  
        else:
            return error
    else:
        return error
   


