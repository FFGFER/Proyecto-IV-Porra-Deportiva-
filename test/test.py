#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
sys.path.append('../src/')

import unittest
import funcionesbasicas


class FuncionesBasicasTest(unittest.TestCase):

    testP = funcionesbasicas.Partidos()
    testA = funcionesbasicas.Apuestas()

    # TEST Partidos ----------------------------------- #
    def testPartidos(self):
        self.assertEqual(self.testP.getPartidos("Cadena"),False,"La jornada debe ser entero")
        self.assertEqual(self.testP.getPartidos(2),[str('Real Madrid FC - Sevilla FC'),str('Atlético de Madrid - FC Barcelona')],"La jornada es correcta")

    def testPartido(self):
        self.assertEqual(self.testP.getPartido(0,"cadena"),False,"La jornada debe ser entero")
        self.assertEqual(self.testP.getPartido("cadena",3),False,"El partido debe ser entero")
        self.assertEqual(self.testP.getPartido(1,2),str('Atlético de Madrid - FC Barcelona'),"El partido es correcto")

    def testSPartidos(self):
        self.assertEqual(self.testP.setPartido("cadena","Leganés - Getafe"),False,"La jornada debe ser entero")
        self.assertEqual(self.testP.setPartido(3,"Leganés - Getafe"),True,"El partido añadido correctamente")
        self.assertEqual(self.testP.setPartido(32,"Leganés - Getafe"),False,"El partido no añadido, jornada no existe")

    def testDelPartidos(self):
        self.assertEqual(self.testP.delPartido("cadena"),False,"La jornada debe ser entero")
        self.assertEqual(self.testP.delPartido(3),True,"El partido borrado correctamente")
        self.assertEqual(self.testP.delPartido(32),False,"El partido no borrado, jornada no existe")


    # TEST Apuestas ----------------------------------- #
    def testApuestas(self):
        self.assertEqual(self.testA.getApuestas("cadena"),False,"Usuario no encontrado")
        self.assertEqual(self.testA.getApuestas("luis14"),[{u'Real Madrid FC - FC Barcelona': u'4-0'}, {u'Atl\xe9tico de Madrid - Betis': u'1-1'}, {u'Sevilla FC - Athletic de Bilbao': u'3-2'}],"Apuestas del usuario luis14 son correctas")


if __name__ == '__main__':
    unittest.main()