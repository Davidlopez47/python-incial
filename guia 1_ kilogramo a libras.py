'''
 ejercicio 1
 Desarrolle un programa que pase un peso de kilogramo a libras teniendo en cuenta que cada kilogramo equivale 
 a 2.2 libras.
'''
#definicion de variables
KILOGRAMO = float()
libra = float()
res = str()
#inicializar variables
KILOGRAMO = 2.2
libra = 0.0
libra = 0.0
#menu en pantalla
res =(input("desea hacer un pasaje de kilogramos a libras? si/no "))
libra= float(input("cuantos kilogramos desea pasar a libras "))

if(res == "si"):
    result = libra * KILOGRAMO
    print(f"los kilogramos pasados a libras son {result}")
else:
    print("ingrese un numero correcto")

'''
prueba de escritorio
1) 24,5 X 2,2 resultado = 53,9✔
2) 74 X 2,2 resultado = 162,8✔
3) 25 x 2,2 resultado = 55,0 ✔
'''