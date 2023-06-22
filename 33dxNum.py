#Cách làm tương tự ở bài 1SoDX.py
def lasoDX(numbers):
    for num in numbers:
        if num<0:
            return False
        so_daonguoc=0
        temp=num
        while temp!=0:
            chuso=temp%10
            so_daonguoc=so_daonguoc*10+chuso
            temp//=10
        if num!=so_daonguoc:
            return False
    return True
def inputList()->list:                  
    n=int(input("Nhập số lượng phần tử: "))            
    result=[]                               
    for i in range (n):                     
        number=int(input("Nhập giá trị phần tử = "))
        result.append(number)                           
    return result
numbers=inputList()
if lasoDX(numbers):
    print("Danh sách đối xứng.")
else:
    print("Danh sách không đối xứng.")