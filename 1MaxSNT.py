#Viết hàm tìm số nguyên tố lớn nhất và nhỏ hơn n được nhập từ bàn phím.
#Ví dụ: n = 20 ----> OUTPUT: 19 (2, 3, 5, 7, 11, 13, 17, 19 < 20)

def tim_SNT_Max(n):                     #Ví dụ: n = 20
    for number in range (n-1,1,-1):         #number chạy từ 19 đến 2, bước nhảy -1 giảm dần
        laNT=True                               #Khai báo ban đầu là True;
        for i in range (2,number):              #i chạy từ 2 tới 19:
            if number%i==0:                         #nếu 19%2==0, không là SNT, trường hợp này 19%2!=0 nên 19 là SNT.
                laNT=False
            break
        if laNT:                                #Nếu là SNT: return number.
            return number
n=int(input("Nhập số n: "))
SNT=tim_SNT_Max(n)
if SNT:
    print("Số nguyên tố lớn nhất nhỏ hơn",n,"là",SNT)
else:
    print("Không có số nguyên tố nhỏ hơn",n)