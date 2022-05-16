import unittest
import xmlrunner
import ekoplaza

collection = ekoplaza.returnOffers()

class TestEkoplaza(unittest.TestCase):

    def test_return_list_ekoplaza(self):
        """
        ✅ Ekoplaza geeft aanbiedingen terug 👉 
        """
        collectionLength = len(collection)
        self.assertTrue(collectionLength != 0)

    def test_list_has_product_title(self):
        """
        ✅ Alle Ekoplaza aanbiedingen hebben een titel 👉 
        """
        for item in collection:
            self.assertTrue(item['product'] != '') # Item heeft een titel

    def test_list_has_product_id(self):
        """
        ✅ Alle Ekoplaza aanbiedingen hebben een productId 👉 
        """
        for item in collection:
            self.assertTrue(item['productId'] != '')         

    def test_list_has_product_deal(self):
        """
        ✅ Alle Ekoplaza aanbiedingen hebben een deal 👉 
        """
        for item in collection:
            self.assertTrue(item['deal'] != '') # Item heeft een deal

    def test_list_has_product_date_start(self):
        """
        ✅ Alle Ekoplaza aanbiedingen hebben een startdatum 👉 
        """
        for item in collection:
            self.assertTrue(item['dateStart'] != '') # Item heeft een startdatum
            
if __name__ == '__main__':
   unittest.main(
        testRunner=xmlrunner.XMLTestRunner(output="."),
        failfast=False,
        buffer=False,
        catchbreak=False,
        verbosity=1)
