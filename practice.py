# Escribir una funcion que convierta un # decimal en binario y otra que convierta # binario en decimal, ingresado por el usuario

# de binario en deciaml
def to_decimal(n):
    n = list(n)
    n.reverse()
    decimal = 0

    # num+=1 es equivalente a decir num=(num+1)
    # num=+1 es equivalente a decir num=(+1)

    for num in range(len(n)):
        decimal += int(n[num]) * 2 ** num
    return decimal

# de decimal a binario
def to_binary(n):
    binary = []
    while n > 0:
        binary.append(str(n % 2))
        n //=2
    binary.reverse()
            #  12 % 2 = 0
            #  6 % 2 = 0
            #  3 % 2 = 1
            #  1 % 2 = 1
            # [0,0,1,1] -> [1,1,0,0]
    return ''.join(binary)


print(to_decimal('1011001'))
print(to_binary(12))
