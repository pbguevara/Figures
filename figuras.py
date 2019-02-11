import math

class Figura():
    def __init__(self):
        pass
    
    def dame_area(self):
        return None
    
    def dame_perimetro(self):
        return None
        
        
class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado
        
    def dame_area(self):
        area = self.lado**2
        return area
        
    def dame_perimetro(self):
        per = 4*self.lado
        return per
        
        
class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        
    def dame_area(self):
        area = self.base*self.altura
        return area
        
    def dame_perimetro(self):
        per = (2*self.base)+(2*self.altura)
        return per
       
        
class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio
        
    def dame_area(self):
        area = math.pi*self.radio**2
        return round(area, 3)
        
    def dame_perimetro(self):
        per = 2*self.radio*math.pi
        return round(per, 3)
        
        
square = Cuadrado(4)
rectangle = Rectangulo(2,6)
circle =Circulo(3)

print(square.dame_area())
print(square.dame_perimetro())

print(rectangle.dame_area())
print(rectangle.dame_perimetro())

print(circle.dame_area())
print(circle.dame_perimetro())
