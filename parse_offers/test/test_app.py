import unittest
import xmlrunner
import os

class TestApp(unittest.TestCase):
    """
    Testen of de GUI bestaat
    """

    def test_app_exists(self):
        """
        ✅ De kortings-app bestaat 👉
        """
        path_src = '../kortings-app/src/'
        self.assertTrue(os.path.isdir(path_src))


if __name__ == '__main__':
    unittest.main(
        testRunner=xmlrunner.XMLTestRunner(output="."),
        failfast=False,
        buffer=False,
        catchbreak=False,
        verbosity=1)
