#Viết hàm để kiểm tra số chính phương

#Lý thuyết số chính phương:
#Số chính phương là số bằng bình phương đúng của một số nguyên.
#Ví dụ: Số 10 không phải là số chính phương, vì căn bậc 2 của 10 bằng 3.16227766017, không phải là số nguyên.

def kt_socp(n):                             #Ví dụ nếu nhập n = 4 (4 là số chính phương)
    if n < 0:                                   
        return False
    sqrt = 0                                    #Xét While (0*0 <= 4: Đúng); Xét If (0*0 != 4: Sai) -> Sqrt = 0 + 1 = 1 
    while sqrt * sqrt <= n:                     #Xét While (1*1 <= 4: Đúng); Xét If (1*1 != 4: Sai) -> Sqrt = 1 + 1 = 2
        if sqrt * sqrt == n:                    #Xét While (2*2 <= 4: Đúng); Xét If (2*2 == 4: Đúng) > Trả về True.
            return True                                                      
        sqrt += 1
    return False
n = int(input("Nhập số cần kiểm tra: "))       #Ví dụ nếu nhập n = 5 (5 không là số chính phương)
if kt_socp(n):                                 #Xét While (0,1,2 <= 4: Đúng); Xét If (0,1,2 != 4: Sai) -> Sqrt = 0 + 1 + 1 + 1 = 3
    print(n, "là số chính phương.")            #Xét While (3*3 >= 4: Sai) ---> Trả về False.
else:
    print(n, "không là số chính phương.")