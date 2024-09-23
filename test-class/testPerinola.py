
import pytest
from perinola import Perinola

def test_prueba():
    assert(True)

def test_cara_inicial():
    perinola = Perinola()
    assert perinola.cara_visible == "Toma 1"

def test_repr():
    perinola = Perinola()
    assert repr(perinola) == "Salió: Toma 1"

def test_tirar():
    perinola = Perinola()
    resultado = perinola.tirar()
    assert resultado in ["Pon 1", "Toma 2", "Todos ponen", "Toma 1", "Pon 2", "Toma todo"]
    assert perinola.cara_visible != "Toma 1"

def test_tirar_multiple():
    perinola = Perinola()
    resultados = [perinola.tirar() for _ in range(100)]
    for resultado in resultados:
        assert resultado in ["Pon 1", "Toma 2", "Todos ponen", "Toma 1", "Pon 2", "Toma todo"]


