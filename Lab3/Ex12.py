#Check if the numbers have different signs
def sign(a,b):
    if (a<0 and b>0) or (a>0 and b<0):
        return True
    return False
#Prints the longest sequence where every 2 consecutive numbers have different signs
def p12(n,l):
    seq = []
    error = "No available sequence"  
    if len(l)<1:
        return error
    else:
        k=1
        startPos = 0
        max = 1
        for i in range(1,n):
            if sign(l[i],l[i-1]) == True:
                k = k+1
            else:
                k=1
            if k>max:
                max = k
                startPos = i - k + 1
        
        i = startPos
        while i<startPos+max:
            seq.append(int(l[i]))
            i = i+1
        return seq