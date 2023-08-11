salir = "salir"

from ejercicios import vehiculo, punto
def execute(opcion):
    if(opcion == "1"):
            kilometraje = input("Ingrese el kilometraje del vehículo")
            velocidad_maxima = input("Ingrese la velocidad máxima del vehículo")
            vVehiculo = vehiculo.Vehiculo(velocidad_maxima, kilometraje)
            print(f"El vehiculo tiene {vVehiculo.kilometraje} kilómetros recorridos con una velocidad máxima de {vVehiculo.velocidad_maxima}")
    elif(opcion == "2"):
         print("opcio 2")

print("1. Clase Vehículo \n 2. Clase Punto, \n 3. Ejecutar métodos de clase Punto \n 4. Clas Rectángulo \n salir para terminar")
while True:
    opcion = input(f"Selecciona la opción a ejecutar.")
    execute(opcion)
    if opcion == salir:
        break



    