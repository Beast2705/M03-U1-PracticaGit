import unittest
from security import validar_password

class TestSecurity(unittest.TestCase):
    def test_password_too_short(self):
        self.assertFalse(validar_password("1234567"))

    def test_password_valid(self):
        self.assertTrue(validar_password("123456789")) # +8 caracteres

if __name__ == '__main__':
    unittest.main()
