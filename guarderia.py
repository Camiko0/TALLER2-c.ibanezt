from models.huron import Huron
from models.boa_constrictor import Boa_Constrictor

class Guarderia():
    def __init__(self) -> None:
        self._huron = [Huron("Rayo", 5.5, 2, "Australia", 10.5), 
                       Huron("Ruby", 6.5, 3, "Australia", 9.5)]
        self._boas = [Boa_Constrictor("Titan", 50.2, 3, "Brasil", 30.5), 
                      Boa_Constrictor("Lulu", 40.2, 3, "Brasil", 25.5)]

    def alimentar_boa(self, boa: Boa_Constrictor):
        try:
            if boa == None:
                return "Esta Boa no existe!"
            else:
                return boa.sumar_ratones_comidos(5)
        except ValueError as error:
            print("Error al alimentar boa: {}".format(error))