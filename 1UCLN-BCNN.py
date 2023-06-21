#Viết hàm tìm UCLN và BCNN của 2 số nguyên a, b (có thể dương và âm)

#Thuật toán Euclid để tìm UCLN:
#Bước 1: Khởi tạo a và b với giá trị tuyệt đối.
#Bước 2: Lặp lại cho đến khi b bằng 0.
#           - Gán giá trị của b cho a.
#           - Tìm phần dư của a chia b và gán kết quả cho b.
#Bước 3: Khi b bằng 0, giá trị của a cuối cùng sẽ là UCLN của a và b.

#Công thức tìm BCNN từ UCLN:BCNN(a,b)=(ab)/UCLN(a,b)

#Note: a,b=b,a%b: Gán từ phải sang trái: b gán cho a, a%b gán cho b

def tim_ucln(a,b):                      #Ví dụ: a = 42 và b = 30
    a=abs(a)                                #a = abs(42) và b = abs(30)
    b=abs(b)                                #Khi b!=0 thì:
    while b!=0:                                 #Gán a = b (a = 30)
        a,b=b,a%b                               #Tính phần dư và gán cho b: b = a%b = 42%30 = 12                        
    return a                                    #Gán a = b (a = 12)
def tim_bcnn(a,b):                              #Tính phần dư và gán cho b: b = a%b = 30%12 = 6
    ucln=tim_ucln(a,b)                          #Gán a = b (a = 6)
    bcnn=abs(a*b)//ucln                         #Tính phần dư và gán cho b: b = a%b = 12%6 = 0
    return bcnn                             #b cuối cùng = 0, xét điều kiện While (không thỏa) ---> Return a (a cuối cùng)
a=int(input("Nhập số nguyên a: "))
b=int(input("Nhập số nguyên b: "))
ucln=tim_ucln(a,b)
bcnn=tim_bcnn(a,b)
print("UCLN của",a,"và",b,"là:",ucln)
print("BCNN của",a,"và",b,"là:",bcnn)