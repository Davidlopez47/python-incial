'''
Escribir un programa que pregunte un nombre de usuario, y que después muestre por pantalla 
si su cantidad de letras es par o impar.
'''
#declarar variables
usuario = str()
result = str()

#inicializar variable
usuario = " "
result = " "

#desarrollo
usuario =input("ingrese su nombre de usuario ")
result = len(usuario)
if (result %2 == 0):
    print(result)
    print("es par")
else:
    print( result)
    print("es impar")


'''
prueba de escritorio:
camilo✔
sol✔
david✔
juan✔
'''

