# Archivo: test_logica_eneagrama.py
import unittest
from logica_eneagrama import LogicaEneagrama

class TestLogicaEneagrama(unittest.TestCase):
    
    def test_eneatipo_mayor(self):
        logica = LogicaEneagrama()
        for i in range(5):
            logica.responder(1)
        for i in range(5):
            logica.responder(0)
        resultado = logica.mostrar_resultado()
        self.assertEqual(resultado, 1)

    def test_responder_incrementa_puntuacion(self):
        logica = LogicaEneagrama()
        self.assertEqual(logica.score[0], 0)
        logica.responder(1)
        self.assertEqual(logica.score[0], 1)

    def test_terminar_cuestionario(self):
        logica = LogicaEneagrama()
        for _ in range(len(logica.preguntas)):
            logica.responder(1)
        self.assertEqual(logica.mostrar_resultado(), 1)

if __name__ == "__main__":
    unittest.main()
