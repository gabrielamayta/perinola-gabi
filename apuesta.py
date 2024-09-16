class Apuesta:
    def __init__(self):
        self.fichas = 0
    def __repr__(self):
        return f"Salio : {self.fichas} fichas"

    def ponerFicha(self, cuantas=1):
        """Agrega una cantidad de fichas especificada (por defecto 1) a la apuesta."""
        self.fichas += cuantas

    def tomarFicha(self, cuantas=1):
        """Quita una cantidad de fichas especificada (por defecto 1) de la apuesta.
        Lanza un error si se intenta sacar más fichas de las que hay.
        """
        if cuantas > self.fichas:
            raise ValueError("No se pueden tomar más fichas de las que hay apostadas.")
        self.fichas -= cuantas

    def tomarTodas(self):
        """Saca todas las fichas de la mesa y devuelve ese número."""
        todas = self.fichas
        self.fichas = 0
        return todas

    def tieneFicha(self, cuantas=1):
        """Devuelve True si hay al menos una cantidad especificada de fichas."""
        return self.fichas >= cuantas

    def estaVacia(self):
        """Devuelve True si no hay fichas en la mesa."""
        return self.fichas == 0

