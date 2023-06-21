#Viết hàm kiểm tra xem số nguyên n có phải là số đối xứng theo trục dọc hay không?
#Ví dụ: 1221 > True; 12212 > False; 1 > True; 122 > False.

def laSoDX(n):
    if n<0:                                                 #n=12321
        return False
    so_dao_nguoc=0                                                         
    temp=n                                                  #temp=12321                                               
    while temp!=0:
        chu_so=temp%10                                      #chs=12321%10 = 1
        so_dao_nguoc=so_dao_nguoc*10+chu_so                 #dn=0*10+1=1
        temp//=10                                           #temp=1232
    return n==so_dao_nguoc                                  
n=int(input("Nhập số nguyên n: "))                          #chs=2   dn=12   temp=123
if laSoDX(n):                                               #chs=3   dn=123  temp=12
    print(n,"là số đối xứng theo trục dọc.")                #chs=2   dn=1232  temp=1
else:                                                       #chs=1   dn=12321  temp=0
    print(n,"không là số đối xứng theo trục dọc.")