import unittest
import xmlrunner
import dirk

collection = dirk.returnOffers()

class TestDirk(unittest.TestCase):

    def test_return_list(self):
        """
        ✅ Dirk geeft aanbiedingen terug 👉 
        """
        collectionLength = len(collection)
        self.assertTrue(collectionLength != 0)

    def test_list_has_product_title(self):
        """
        ✅ Alle Dirk aanbiedingen hebben een titel 👉 
        """
        for item in collection:
            self.assertTrue(item['product'] != '') # Item heeft een titel

    def test_list_has_product_id(self):
        """
        ✅ Alle Dirk aanbiedingen hebben een productId 👉 
        """
        for item in collection:
            self.assertTrue(item['productId'] != '')               

    def test_list_has_product_deal(self):
        """
        ✅ Alle Dirk aanbiedingen hebben een deal 👉 
        """
        for item in collection:
            self.assertTrue(item['deal'] != '') # Item heeft een deal

    def test_list_has_product_date_start(self):
        """
        ✅ Alle Dirk aanbiedingen hebben een startdatum 👉 
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