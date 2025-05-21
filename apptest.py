import unittest
import app

class TestAppFunctions(unittest.TestCase):

    def test_is_even(self):
        self.assertTrue(app.is_even(2))
        self.assertFalse(app.is_even(3))
        self.assertTrue(app.is_even(0))
        self.assertTrue(app.is_even(-4))

    def test_is_odd(self):
        self.assertTrue(app.is_odd(1))
        self.assertFalse(app.is_odd(2))
        self.assertFalse(app.is_odd(0))
        self.assertTrue(app.is_odd(-5))

if __name__ == '__main__':
    unittest.main()
