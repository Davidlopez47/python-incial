'''
Ciclistas: La final de una carrera de ciclistas tiene n competidores
(n se ingresa por teclado). Desarrollar un programa que permita cargar, por cada competidor,
nombre y tiempo de carrera.
'''
import random
i = 0
cantidad = int(0);
competidor = int(0);
nombre = int(0);
tiempo_carrera = int(0);
ganador = int(0)
 
competidor = int(input(" cuantos competidores van a participar? "));
tiempo_carrera = int(input("cuanto va durar la carrera? "))

while i < competidor:
    nombre = input("ingrese un  nombre ")
    i += 1
    cantidad = random.randint(20,60)
    print(f"el competidor {nombre} tuvo un tiempo de {cantidad} minutos")
   
    
 
if cantidad > tiempo_carrera:
    print(f"el ganador es {nombre}")   
elif cantidad < tiempo_carrera:
    print("el ganador no supero el tiempo record")
elif cantidad >= tiempo_carrera:
    print("el ganador supero o igualo el tiempo record" )

    


