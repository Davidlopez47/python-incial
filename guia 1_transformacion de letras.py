'''
Escriba un programa que transforme todas las letras de una palabra en mayúsculas
minúsculas y la primera con minúsculas
'''
#declarar variables
res = str()
pregunt = str()

#definir variable()
res = " "
pregunt = " "
#procedimiento


print('''
-----------------------------
-1) todo mayusculas         -
-2) todo minuscula          -
-3) primera letra mayuscula -
-4) los 3 al mismo tiempo   -
-----------------------------
''')
pregunt = int(input("escriba su respuesta "))
res = input("escriba lo primero que se le ocurra ")
if(pregunt == 1):
    print(res.upper())
elif(pregunt == 2):
    print(res.lower())
elif(pregunt == 3):
    print(res.capitalize())
elif(pregunt == 4):
    print(res.upper())
    print(res.lower())
    print(res.capitalize())
else:
    print("intente probar con un numero entre el 1 y el 4")
    
    
'''
prueba de escritorio:
hola profe✔
juan✔
hola como estas✔
'''