from models.animal import Animal

#Clase Huron que implementa de Animal con los metodos abstractos implementados
class Perro(Animal):
    def __init__(self) -> None:
        self._nombre = ""
    
    # Metodos implementados
    def hacer_sonido(self) -> str:
        return "¡Wow Wow!"