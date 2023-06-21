#Viết hàm python đảo ngược số nguyên dương n.

def reverse_number(n):                          #Ví dụ: n = 123 
    dao_nguoc=0                                     #dao_nguoc = 0
    while n>0:                                      #n = 123 > 0 
        chu_so=n%10                                     #chu_so = 123 / 10 dư 3 ---> chu_so = 3
        dao_nguoc=dao_nguoc*10+chu_so                   #dao_nguoc = 0*10+3 = 3
        n//=10                                          #n = 123 / 10 = 12
    return dao_nguoc                                #n = 12 > 0
n=int(input("Nhập số nguyên dương n: "))                #chu_so = 12 / 10 dư 2 ---> chu_so = 2
soDaoNguoc=reverse_number(n)                            #dao_nguoc = 3*10+2 = 32
print("Số đảo ngược của",n,"là",soDaoNguoc)             #n = 12 / 10 = 1
                                                    #n = 1 > 0
                                                        #chu_so = 1 / 10 dư 1 ---> chu_so = 1
                                                        #dao_nguoc = 32*10+1 = 321
                                                        #n = 1/10 = 0
                                                    #n = 0 (không thỏa While)
                                                    #return dao_nguoc