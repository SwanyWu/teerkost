import unittest

import albertheijn

class TestAlbertHeijn(unittest.TestCase):

    def test_return_list_albertheijn(self):
        """
        ✅ Albert Heijn geeft aanbiedingen terug 👉 
        """
        collectionLength = len(albertheijn.returnOffers())
        self.assertTrue(collectionLength != 0)

if __name__ == '__main__':
    unittest.main(verbosity=0)
