print("Fibonacci")
print("Seleccione el numero hasta el que quiere mostrar la secuencia de Fibonacci")
last = int(raw_input("Numero:"))

a = 1
b = 2
cadena = '1'
while b <= last:
    cadena += ', ' + str(b)
    temp = b
    b = b + a
    a = temp
print cadena

