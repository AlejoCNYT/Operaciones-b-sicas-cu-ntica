from math import sqrt
import Libcplx as lc
import unittest

class TestCplxOperations(unittest.TestCase):

    def test_cplxsum(self):
        suma =  lc.cplxsum((3,5),(-2.6,6.8))
        self.assertAlmostEqual(suma[0], 0.4)
        self.assertAlmostEqual(suma[1], 11.8)

    def test_cplxproduct(self):
        producto =  lc.cplxproduct((3,-1), (1,4))
        self.assertAlmostEqual(producto[0], 7)
        self.assertAlmostEqual(producto[1], 11)

    def test_cplxsust(self):
        sustraccion =  lc.cplxsust((3,5), (-2.6,6.8))
        self.assertAlmostEqual(sustraccion[0], 5.6)
        self.assertAlmostEqual(sustraccion[1], -1.8)

    def test_cplxcoc(self):
        cociente =  lc.cplxcoc((-2,1), (1,2))
        self.assertAlmostEqual(cociente[0], 0)
        self.assertAlmostEqual(cociente[1], 1)

    def test_cplxmod(self):
        modulo =  lc.cplxmod(2,1)
        self.assertAlmostEqual(modulo, sqrt(5))

    def test_cplxconj(self):
        conjunto =  lc.cplxconj(2,3)
        self.assertAlmostEqual(conjunto[0], 2)
        self.assertAlmostEqual(conjunto[1], -3)

    def test_cplxpolaracartesiana(self):
        cart =  lc.cplxpolaracartesiana(sqrt(2), 45)
        self.assertAlmostEqual(cart[0], 1)
        self.assertAlmostEqual(cart[1], 1)

    def test_cplxcartesianaapolar(self):
        pol =  lc.cplxcartesianaapolar(1, 1)
        self.assertAlmostEqual(pol[0], sqrt(2))
        self.assertAlmostEqual(pol[1], 45)

    def test_cplxfase(self):
        grados =  lc.cplxfase(1,1)
        self.assertAlmostEqual(grados, 45.0)

if __name__ == '__main__':
    unittest.main()
