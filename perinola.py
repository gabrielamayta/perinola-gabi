class Perinola:
   def __init__(self):
           self.cara_visible = "Toma 1"
           def __repr__(self):
                return f"Salio : {self.cara_visible}"
           def tirar(self):
                caras = ("Pon 1", "Toma 2","Todos ponen"," Toma 1", "Pon 2","Toma todo")
                self.cara_visible = choices(caras)
                return self.cara_visible
           

           # Ejemplo de uso
perinola = Perinola()
print(perinola)  # Muestra la cara inicial
print(perinola.tirar())  # Cambia la cara visible y muestra el resultado
print(perinola)  # Muestra la nueva cara visible después de tirar
