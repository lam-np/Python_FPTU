def inputList()->list:                                  #Hàm trả về kết quả kiểu list (danh sách)
    n=int(input("Input n = "))
    result=[]
    for i in range (n):
        number=int(input("Input your number = "))
        result.append(number)                           #Phương thức 'append': thêm vào phần tử cuối trong danh sách
    return result
def isPrime(number):
    if number<=1:
        return False
    for i in range (2,int(number**0.5)+1):
        if number%i==0:
            return False
    return True
def sumOfPrime(a:list)->int:
    primeNum=0
    for number in a:
        if isPrime(number):
            primeNum+=1
    return primeNum
a=inputList()
print(a)
print(sumOfPrime(a))