from datetime import datetime
import unittest
import xmlrunner
import spar

collection = spar.return_offers()

class TestSpar(unittest.TestCase):
    """
    Testen van het ophalen van Spar aanbiedingen
    """

    def test_return_list_spar(self):
        """
        ✅ Spar geeft aanbiedingen terug 👉
        """
        collection_length = len(collection)
        self.assertTrue(collection_length != 0)

    def test_list_has_product_title(self):
        """
        ✅ Alle Spar aanbiedingen hebben een titel 👉
        """
        for item in collection:
            self.assertTrue(item['product'] != '')

    def test_list_has_product_id(self):
        """
        ✅ Alle Spar aanbiedingen hebben een productId 👉
        """
        for item in collection:
            self.assertTrue(item['productId'] != '')

    def test_list_has_product_deal(self):
        """
        ✅ Alle Spar aanbiedingen hebben een deal 👉
        """
        for item in collection:
            self.assertTrue(item['deal'] != '')

    def test_list_prices_are_numbers(self):
        """
        ✅ Alle prijzen zijn een nummer 👉
        """
        for item in collection:
            self.assertTrue(isinstance(item['price'], float))

    def test_list_has_valid_date_start(self):
        """
        ✅ Alle aanbiedingen hebben een valide startdatum 👉
        """
        for item in collection:
            self.assertTrue(item['dateStart'] != '') # Item heeft een startdatum
            try:
                dt_object = datetime.strptime(item['dateStart'], "%Y-%m-%d")
                self.assertTrue(isinstance(dt_object, datetime))
            except:    
                raise AssertionError ("dateStart '"+ item['dateStart'] + "' cannot be converted into a datetime object.")

if __name__ == '__main__':
    unittest.main(
        testRunner=xmlrunner.XMLTestRunner(output="."),
        failfast=False,
        buffer=False,
        catchbreak=False,
        verbosity=1)
