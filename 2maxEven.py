def inputList()->list:                                  #Hàm trả về kết quả kiểu list (danh sách)
    n=int(input("Input n = "))
    result=[]
    for i in range (n):
        number=int(input("Input your number = "))
        result.append(number)                           #Phương thức 'append': thêm vào phần tử cuối trong danh sách
    return result

def findMaxEven():
    danhsach=inputList()
    maxEven=0
    for number in danhsach:
        if number%2==0 and number>maxEven:
            maxEven=number
    return maxEven
max_even=findMaxEven()
if max_even==0:
    print("There are no even numbers in the list!")
else:
    print("The largest even number in the list is:",max_even)