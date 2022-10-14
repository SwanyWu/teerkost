import unittest
import xmlrunner
import os

class test_app(unittest.TestCase):
    """
    Testen of de GUI bestaat
    """

    def test_app_exists(self):
        """
        ✅ De kortings-app bestaat 👉
        """
        PATH_SRC = '../kortings-app/src/'
        self.assertTrue(os.path.isdir(PATH_SRC))


if __name__ == '__main__':
    unittest.main(
        testRunner=xmlrunner.XMLTestRunner(output="."),
        failfast=False,
        buffer=False,
        catchbreak=False,
        verbosity=1)
