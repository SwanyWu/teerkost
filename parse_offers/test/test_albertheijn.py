import unittest

import albertheijn

class TestAlbertHeijn(unittest.TestCase):

    def test_return_list_albertheijn(self):
        """
        ✅ Albert Heijn geeft aanbiedingen terug 👉 
        """
        collectionLength = len(albertheijn.returnOffers())
        self.assertTrue(collectionLength != 0)

    def test_list_has_product_title(self):
        """
        ✅ Alle Albert Heijn aanbiedingen hebben een titel 👉 
        """
        collection = albertheijn.returnOffers()
        for item in collection:
            self.assertTrue(item['product'] != '') # Item heeft een titel

    def test_list_has_product_deal(self):
        """
        ✅ Alle Albert Heijn aanbiedingen hebben een deal 👉 
        """
        collection = albertheijn.returnOffers()
        for item in collection:
            self.assertTrue(item['deal'] != '') # Item heeft een deal

    def test_list_has_product_date_start(self):
        """
        ✅ Alle Albert Heijn aanbiedingen hebben een startdatum 👉 
        """
        collection = albertheijn.returnOffers()
        for item in collection:
            self.assertTrue(item['dateStart'] != '') # Item heeft een startdatum
            
if __name__ == '__main__':
    unittest.main(verbosity=0)
