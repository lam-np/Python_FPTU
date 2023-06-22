def inputList():                               
    n=int(input("Input n = "))
    a=[]
    for i in range (n):
        number=int(input("Input your number = "))
        a.append(number)                           #Phương thức 'append': thêm vào phần tử cuối trong danh sách
    return a
def isPrime(number):
    if number<=1:
        return False
    for i in range (2,int(number**0.5)+1):
        if number%i==0:
            return False
    return True
fa=inputList()
def getNPrime(a:list,fn:int):                                   
    b=[]                                                        
    fc=0                                    
    k=0
    while fc<fn or k>len(fa):               
        while not isPrime(a[k]):              
            k+=1            
        b.append(a[k])                      
        k+=1                                
        fc+=1
    return b
fnn=int(input("Enter x numbers of primes to output: "))
print(getNPrime(fa,fnn))