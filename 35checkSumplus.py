def inputList()->list:                  
    n=int(input("Nhập số lượng phần tử: "))            
    result=[]                               
    for i in range (n):                     
        number=int(input("Nhập giá trị phần tử = "))
        result.append(number)                           
    return result
def tongBang(numbers):
    tong_cong = sum(numbers)
    tong_trai = 0
    for i in range(len(numbers)):
        tong_phai=tong_cong
        tong_cong -= numbers[i]
        if tong_trai == tong_cong:
            return True
        tong_trai += numbers[i]
    return False
numbers=inputList()
if tongBang(numbers):
    print("True")
else:
    print("False")
number=int(input("Nhập số muốn thêm vào danh sách: "))
numbers.append(number)
if tongBang(numbers):
    print("True")
else:
    print("False")