import unittest
import os

class TestApp(unittest.TestCase):

    def test_app_exists(self):
        """
        ✅ De kortings-app bestaat 👉 
        """
        pathForJson = '../kortings-app/src/'
        self.assertTrue(os.path.isdir(pathForJson))


if __name__ == '__main__':
    unittest.main(verbosity=0)
