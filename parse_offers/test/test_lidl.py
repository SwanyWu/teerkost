import unittest

import lidl

class TestLidl(unittest.TestCase):

    def test_return_list_lidl(self):
        """
        ✅ Lidl geeft aanbiedingen terug 👉 
        """
        collectionLength = len(lidl.returnOffers())
        self.assertTrue(collectionLength != 0) # lidl geeft resultaten terug    


if __name__ == '__main__':
    unittest.main(verbosity=0)
