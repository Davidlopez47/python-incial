'''
Multiplicación. Ingresar un número cualquiera por teclado y que muestre su respectiva
tabla del 1 al 10
'''
factor = int(0)
desde = int(1)
hasta = int(10)

factor = int(input("ingrese un numero "))
for f in range(desde, hasta + 1):
    print(f'{factor} x {f} = {factor * f}')