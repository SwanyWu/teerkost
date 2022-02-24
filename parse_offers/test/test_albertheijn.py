import unittest

import albertheijn

class TestAlbertHeijn(unittest.TestCase):

    def test_return_list_albertheijn(self):
        collectionLength = len(albertheijn.returnOffers())
        self.assertTrue(collectionLength != 0) # albertheijn geeft resultaten terug

if __name__ == '__main__':
    unittest.main()
