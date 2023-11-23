def nombre_premier(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+ 
1):
        if num % i == 0:
            return False
    return True
for num in range(2, 1001):
    if nombre_premier(num):
            print(num)