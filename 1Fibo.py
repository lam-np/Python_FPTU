def Fibo(n):
    a=0
    b=1
    if n==0:
        return a
    elif n==1:
        return str(a) + " " + str(b)
    chuoi_fibo = str(a) + " " + str(b)
    for i in range (2,n+1):
        c = a + b
        chuoi_fibo += " " + str(c)
        a = b
        b = c
    return chuoi_fibo
n = int(input("Enter n: "))
ket_qua = Fibo(n)
print(ket_qua)