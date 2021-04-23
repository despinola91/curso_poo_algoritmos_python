class CasillaDeVotacion:

    def __init__(self, identificador, pais):
        self.__identificador = identificador
        self.__pais = pais
        self.__region = None

    @property #Con esto le indicamos que la función que sigue se comportará como un atributo para obtener el valor de __region --> getter
    def region(self):
        return self.__region

    @region.setter #Con esto le indicamos que la función que sige se comportará como un atributo para setear el valor de __region --> setter
    def region(self, region):
        if region in self.__pais:
            self.__region = region
        else:
            raise ValueError(f'La region {region} no es valida en {self.__pais}')

casilla = CasillaDeVotacion(123, ["Ciudad de Mexico", "Morelos"])
print(casilla.region)
casilla.region = "Ciudad de Mexico"
print(casilla.region)