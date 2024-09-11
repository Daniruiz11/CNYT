#PRUEBAS

import unittest
import Libreria
import math

class unit_Libreria(unittest.TestCase):
    '-----------------------------------Operaciones básicas-----------------------------------'
    
    # Pruebas para la adición.
    def test_adicionar(self):
        self.assertEqual(Libreria.adicionar((3,7),(2,4)),(5,11))
        self.assertEqual(Libreria.adicionar((6,-2),(1,3)),(7,1))

    # Pruebas para la sustracción.
    def test_sustraer(self):
        self.assertEqual(Libreria.sustraer((5,8),(3,6)),(2,2))
        self.assertEqual(Libreria.sustraer((7,-1),(4,-4)),(3,3))

    # Pruebas para la multiplicación.
    def test_multiplicar(self):
        self.assertEqual(Libreria.multiplicar((1,4),(2,-3)),(14,5))
        self.assertEqual(Libreria.multiplicar((-3,2),(-1,5)),(-7,-17))

    # Pruebas para el conjugado.
    def test_conjugado(self):
        self.assertEqual(Libreria.conjugado((3,-4)),(3,4))
        self.assertEqual(Libreria.conjugado((0,5)),(0,-5))

    # Pruebas para la magnitud.
    def test_magnitud(self):
        self.assertEqual(Libreria.magnitud((1,1)),math.sqrt(2))
        self.assertEqual(Libreria.magnitud((2,-2)),math.sqrt(8))

    def test_dividir(self):
        resultado = Libreria.dividir((7,3),(2,-2))
        self.assertAlmostEqual(resultado[0], 1.0)
        self.assertAlmostEqual(resultado[1], 2.5)

    # Pruebas para la conversión de representación polar a cartesiana.
    def test_polar_a_cartesiano(self):
        resultado = Libreria.polar_a_cartesiano((5,math.pi/4))
        self.assertAlmostEqual(resultado[0], 3.5355339059327378)
        self.assertAlmostEqual(resultado[1], 3.5355339059327378)

    # Pruebas para la conversión de representación cartesiana a polar.
    def test_cartesiano_a_polar(self):
        self.assertEqual(Libreria.cartesiano_a_polar((1,-1)),(math.sqrt(2),315.0))
        self.assertEqual(Libreria.cartesiano_a_polar((-2,2)),(math.sqrt(8),135.0))

    # Pruebas para la fase.
    def test_fase(self):
        self.assertEqual(Libreria.fase((2,2)),(45.0))
        self.assertEqual(Libreria.fase((-2,-2)),(225.0))
        self.assertEqual(Libreria.fase((0,-3)),(270.0))
        self.assertEqual(Libreria.fase((0,3)),(90.0))

if __name__ == '__main__':
    unittest.main()
