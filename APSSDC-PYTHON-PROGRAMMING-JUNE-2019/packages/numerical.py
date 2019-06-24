def numberprimefactors(n):
    if isprime(n):
        return 1
    count=0
    for i in range(2,n//2+1):
        if isprime(i) and n%i ==0:
            count+=1
    return count



def isprime(n):
    flag=1
    if n==2:
        return True
    for i in range (2,n//2+1):
        if n%i==0:
            flag=0
            return False
    if flag==1:
        return True
def countofdigits(s):
    charcount=0
    digitcount=0
    for i in range(0,len(s)):
        if((ord(s[i])>=97 and ord(s[i])<=122)or (ord(s[i])>=65 and ord(s[i])<=90)):
            charcount=charcount+1
        elif(ord(s[i])>=48 and ord(s[i])<=57):
            
            digitcount=digitcount+1
    print(charcount)
    print(digitcount)