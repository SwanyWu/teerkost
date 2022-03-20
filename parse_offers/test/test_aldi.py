import unittest

import aldi

class TestAldi(unittest.TestCase):

    def test_return_list(self):
        """
        ✅ Aldi geeft aanbiedingen terug 👉 
        """
        collectionLength = len(aldi.returnOffers())
        self.assertTrue(collectionLength != 0)

    def test_list_has_product_title(self):
        """
        ✅ Alle Aldi aanbiedingen hebben een titel 👉 
        """
        collection = aldi.returnOffers()
        for item in collection:
            self.assertTrue(item['product'] != '') # Item heeft een titel

    def test_list_has_product_deal(self):
        """
        ✅ Alle Aldi aanbiedingen hebben een deal 👉 
        """
        collection = aldi.returnOffers()
        for item in collection:
            self.assertTrue(item['deal'] != '') # Item heeft een deal

    def test_list_has_product_date_start(self):
        """
        ✅ Alle Aldi aanbiedingen hebben een startdatum 👉 
        """
        collection = aldi.returnOffers()
        for item in collection:
            self.assertTrue(item['dateStart'] != '') # Item heeft een startdatum
            
if __name__ == '__main__':
    unittest.main(verbosity=0)
