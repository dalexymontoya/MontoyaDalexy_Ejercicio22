# Referencias http://katyhuff.github.io/python-testing/
# https://docs.python.org/2/library/unittest.html

import unittest
import complejo
import math

class TestComplejo(unittest.TestCase):
    def test_conjugado(self):
        c = complejo.Complejo(2.0,5.0)
        c.conjugado()
        self.assertEqual(c.imaginario, -5.0)

        c = complejo.Complejo(2.0,-2.8)
        c.conjugado()
        self.assertEqual(c.imaginario, 2.8)

    def test_norma(self):
        c = complejo.Complejo(0,1.0)
        c.calcula_norma()
        self.assertEqual(c.norma, 1.0)
        c = complejo.Complejo(1.0,0.0)
        c.calcula_norma()
        self.assertEqual(c.norma, 1.0)

        c = complejo.Complejo(5.0,5.0)
        c.calcula_norma()
        self.assertAlmostEqual(c.norma, math.sqrt(50.0))

    def test_pow(self):
        c = complejo.Complejo(0, 1.0) #esto es i
        d = c.pow(2)
        self.assertAlmostEqual(d.real,-1.0) #por eso i al cuadrado es -1
        self.assertAlmostEqual(d.imaginario,0.0)

        c = complejo.Complejo(1.0, 1.0)
        d = c.pow(6)
        self.assertAlmostEqual(d.real,0.0)
        self.assertAlmostEqual(d.imaginario,-8.0)
        
        
    def testmulti (self):
        
        c = complejo.Complejo(8, 6.0)
        a = complejo.Complejo(2, 2.0)
        d = c.mult(a)
        self.assertAlmostEqual(d.real, 4)
        self.assertAlmostEqual(d.imaginario, 28)
        
        
        c1 = complejo.Complejo(2, 2.0)
        a1 = complejo.Complejo(3, 1.0)
        d1 = c1.mult(a1)
        self.assertAlmostEqual(d1.real, 4)
        self.assertAlmostEqual(d1.imaginario, 8) 


if __name__ == '__main__':
    unittest.main()
    
# este archivo se debe utilizar como 'python -m unittest -v pruebas'
