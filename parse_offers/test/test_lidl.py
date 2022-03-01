import unittest

import lidl

class TestLidl(unittest.TestCase):

    def test_return_list_lidl(self):
        """
        ✅ Lidl geeft aanbiedingen terug 👉 
        """
        collectionLength = len(lidl.returnOffers())
        self.assertTrue(collectionLength != 0) # lidl geeft resultaten terug    

    def test_list_has_product_title(self):
        """
        ✅ Alle Lidl aanbiedingen hebben een titel 👉 
        """
        collection = lidl.returnOffers()
        for item in collection:
            self.assertTrue(item['product'] != '') # Item heeft een titel

    def test_list_has_product_deal(self):
        """
        ✅ Alle Lidl aanbiedingen hebben een deal 👉 
        """
        collection = lidl.returnOffers()
        for item in collection:
            self.assertTrue(item['deal'] != '') # Item heeft een deal

    def test_list_has_product_date_start(self):
        """
        ✅ Alle Lidl aanbiedingen hebben een startdatum 👉 
        """
        collection = lidl.returnOffers()
        for item in collection:
            self.assertTrue(item['dateStart'] != '') # Item heeft een startdatum

if __name__ == '__main__':
    unittest.main(verbosity=0)
