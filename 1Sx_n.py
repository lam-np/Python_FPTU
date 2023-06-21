#Viết hàm nhập vào x và n, tính S(x,n) = x^1/1! + x^2/2! + ... + x^n/n!

#Note: x**i = x^i

def tinhGT(k):
    giai_thua=1
    for i in range (1,k+1):
        giai_thua*=i
    return giai_thua
def tinhS(x,n):
    S=0
    for i in range (1,n+1):
        S+=(x**i)/tinhGT(i)     
    return S
x=float(input("Nhập x: "))
n=int(input("Nhập n: "))
ket_qua=tinhS(x,n)
print("Giá trị của S(x,n) là:",ket_qua)