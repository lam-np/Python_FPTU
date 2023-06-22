def isIncreasingList(a: list) -> bool:      
    for i in range(1, len(a)):
        if a[i] <= a[i-1]:
            return False
    return True
n = int(input("Input n = "))

a = []
for i in range(n):
    number = int(input("Input your number: "))
    a.append(number)
result = isIncreasingList(a)
print(result)