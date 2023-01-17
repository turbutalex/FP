# Returns the biggest number that can be formed with ns figures
def maxNumber(n):
    l = [0,0,0,0,0,0,0,0,0,0,0]
    m=0
    
    while(n):
            l[int(n%10)] = l[int(n%10)]+1
            n = int(n/10)
    
    for i in range(9,-1,-1):
        while(l[i]!=0):
            m=m*10+i
            l[i]=l[i]-1
    return m

print(maxNumber(6700))

