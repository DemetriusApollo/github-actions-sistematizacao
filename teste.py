import unittest 

from main import helloword

class Testes(unittest.TesteCase):

    def teste_hello(self):
        self.assertEqual(helloword(),'Olá mundo')

if __name__ == '__main__':
    unittest.main()