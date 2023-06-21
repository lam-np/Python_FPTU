a = int(input("a= "))
b = int(input("b= "))
def UCLN(a,b):
    a=abs(a)                                            
    b=abs(b)                                            
    for number in range (1,a+1):                                     
        if(a%number==0)and(b%number==0):                    
            UCLN=number                                         
    return UCLN      
                                 
ucln=UCLN(a,b)                                          
print("UCLN=",ucln)    
def BCNN(a,b):
    bcnn=abs(a*b)//ucln
    return bcnn
bcnn=BCNN(a,b)
print("BCNN=",bcnn)