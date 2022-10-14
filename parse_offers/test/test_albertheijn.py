import unittest
import xmlrunner
import albertheijn

collection = albertheijn.return_offers()

class test_albertheijn(unittest.TestCase):

    def test_return_list_albertheijn(self):
        """
        ✅ Albert Heijn geeft aanbiedingen terug 👉 
        """
        collectionLength = len(collection)
        self.assertTrue(collectionLength != 0)

    def test_list_has_product_title(self):
        """
        ✅ Alle Albert Heijn aanbiedingen hebben een titel 👉 
        """
        for item in collection:
            self.assertTrue(item['product'] != '')

    def test_list_prices_are_numbers(self):
        """
        ✅ Alle prijzen zijn een nummer 👉 
        """
        for item in collection:
            self.assertTrue(isinstance(item['price'], float))      

    def test_list_has_product_id(self):
        """
        ✅ Alle Albert Heijn aanbiedingen hebben een productId 👉 
        """
        for item in collection:
            self.assertTrue(item['productId'] != '')         

    def test_list_has_product_deal(self):
        """
        ✅ Alle Albert Heijn aanbiedingen hebben een deal 👉 
        """
        for item in collection:
            self.assertTrue(item['deal'] != '') # Item heeft een deal

    def test_list_has_product_date_start(self):
        """
        ✅ Alle Albert Heijn aanbiedingen hebben een startdatum 👉 
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
