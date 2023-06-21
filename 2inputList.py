#Tạo list
def inputList()->list:                                  #Hàm trả về kết quả kiểu list (danh sách)
    n=int(input("Input n = "))
    result=[]
    for i in range (n):
        number=int(input("Input your number = "))
        result.append(number)                           #Phương thức 'append': thêm vào phần tử cuối trong danh sách
    return result
a=inputList()
print(a)