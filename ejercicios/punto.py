import math
class Punto:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
    
    def mostrar(self):
        print(f"(x: {self.x}, y:{self.y})")
    
    def mover(self, x, y):
        self.x = x
        self.y = y
    def calcular_distancia(self, x, y):
        # d=√((x_2-x_1)²+(y_2-y_1)²)
        distancia = math.sqrt(math.pow(x-self.x)+math.pow(y-self.y))
        print(f"La distancia de los dos puntos es {distancia}")