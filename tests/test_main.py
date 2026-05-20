# tests/test_main.py

import unittest
from main import dividir, saudacao


class TestMain(unittest.TestCase):

    def test_dividir(self):
        self.assertEqual(dividir(10, 2), 5)

    def test_saudacao(self):
        self.assertEqual(
            saudacao("Gabriel"),
            "Olá, Gabriel!"
        )


if __name__ == "__main__":
    unittest.main()