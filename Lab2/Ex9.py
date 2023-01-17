#Return the palindrome of n
def palindrome(n):
    m=0
    while n:
        m=m*10+n%10
        n=int(n/10)
    return m

print(palindrome(123456))  