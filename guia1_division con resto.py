'''
División con resto. Plantear un algoritmo que permita informar, para dos valores a y b el 
resultado de la división a/b y el resto de esa división
''' 
#declarar variable
num_1 = float()
num_2 = float()

#inicializar variable
div = 0.0
div2 = 0.0
num_1 = 0.0
num_2 = 0.0
#mostrar en pantalla
num_1 = float(input("ingrese el primer numero que desea divir "))
num_2 = float(input("ingrese el segundo numero que desea divir "))

div1 = num_1 / num_2
div2 = num_1 % num_2

print(f"el resultado de la  divisiones es de {div1}")
print(f"el resto de la division es de {div2}")
