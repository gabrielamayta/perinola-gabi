import random  

class Perinola:
    def __init__(self):
        self.cara_visible = "Toma 1"

    def __repr__(self):
        return f"Salió: {self.cara_visible}"

    def tirar(self):
        caras = ("Pon 1", "Toma 2", "Todos ponen", "Toma 1", "Pon 2", "Toma todo")
        self.cara_visible = random.choice(caras)  
        return self.cara_visible
    



perinola = Perinola()
print(perinola)  
print(perinola.tirar())  
print(perinola)  
