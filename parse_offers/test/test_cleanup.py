import unittest
import xmlrunner
from cleanup import categorize, cleantext, giveid

class test_cleanup(unittest.TestCase):
    """
    Testen van de cleanup module
    """

    def test_return_category_but_ignore_words(self):
        """
        ✅ Categorie voor product vinden maar ook woorden negeren 👉
        """
        resulting_category = categorize.find_category_for_product("een biefstuk", "bla bla")
        self.assertTrue(resulting_category == 'vlees')

        resulting_category = categorize.find_category_for_product("een vegan", "bla bla")
        self.assertTrue(resulting_category == 'vegan')

        resulting_category = categorize.find_category_for_product("een vegan biefstuk", "bla bla")
        self.assertTrue(resulting_category == 'vegan')

        resulting_category = categorize.find_category_for_product("een biefstuk vegan", "bla bla")
        self.assertTrue(resulting_category == 'vegan')

        resulting_category = categorize.find_category_for_product("een biefstuk vegan biefstuk", "bla bla")
        self.assertTrue(resulting_category == 'vegan')

        resulting_category = categorize.find_category_for_product("calvé saus", "bla bla")
        self.assertTrue(resulting_category != 'beleg')

    def test_return_category_none_found(self):
        resulting_category = categorize.find_category_for_product("derpie derp", "")
        self.assertTrue(resulting_category == 'geen-categorie')

        resulting_category = categorize.find_category_for_product("", "derpie derp")
        self.assertTrue(resulting_category == 'geen-categorie')

        resulting_category = categorize.find_category_for_product("", "")
        self.assertTrue(resulting_category == 'geen-categorie')

    def test_return_category_by_title(self):
        """
        ✅ Categorie voor product wordt gevonden in titel 👉
        """
        resulting_category = categorize.find_category_for_product("bier water", "een flesje")
        self.assertTrue(resulting_category == 'bier')

    def test_return_category_by_description(self):
        """
        ✅ Categorie voor product wordt gevonden in beschrijving 👉
        """
        resulting_category = categorize.find_category_for_product("een flesje", "water bier")
        self.assertTrue(resulting_category == 'bier')

    def test_return_category_w_empty_title(self):
        """
        ✅ Categorie voor product wordt gevonden met ontbrekende titel 👉
        """
        resulting_category = categorize.find_category_for_product("", "bier")
        self.assertTrue(resulting_category == 'bier')

    def test_return_category_w_empty_description(self):
        """
        ✅ Categorie voor product wordt gevonden met ontbrekende beschrijving 👉
        """
        resulting_category = categorize.find_category_for_product("bier", "")
        self.assertTrue(resulting_category == 'bier')

    def test_return_single_word_capitalized(self):
        """
        ✅ Categorie voor product wordt gevonden met enkel woord en hoofdletter 👉
        """
        resulting_category = categorize.find_category_for_product("Lenor", "derp derp")
        self.assertTrue(resulting_category == 'huishouden')

    def test_return_single_word_w_apostrof(self):
        """
        ✅ Categorie voor product wordt gevonden met enkel woord en apostrof 👉
        """
        resulting_category = categorize.find_category_for_product("Mango's Ready to Eat", "2-pack")
        self.assertTrue(resulting_category == 'fruit')

    def test_return_category_found_by_multiple_keyword_string(self):
        """
        ✅ Categorie voor product wordt gevonden op basis van meerdere woorden in een string 👉
        """
        resulting_category = categorize.find_category_for_product("Een friesche vlag latte pak", "2-pack")
        self.assertTrue(resulting_category == 'zuivel')

    def test_clean_title(self):
        """
        ✅ Titel van een product is netjes 👉
        """
        clean_title = cleantext.clean_up_title("Jumbo Alle AH bananen* met schil ")
        expected_title = "Bananen met schil"
        self.assertEqual(clean_title, expected_title)

    def test_clean_info(self):
        """
        ✅ Productinfo van een product is netjes 👉
        """
        clean_info_text = cleantext.clean_up_info("Alle soorten 300 gram")
        expected_info_text = "300 gram"
        self.assertEqual(clean_info_text, expected_info_text)

        clean_info_text = cleantext.clean_up_info("Bijv. de groene soort")
        expected_info_text = ""
        self.assertEqual(clean_info_text, expected_info_text)

    def test_give_id(self):
        """
        ✅ Product van een eigen ID voorzien 👉
        """
        test_offer_object = [{
            'product': 'Luxe stol',
            'productInfo': '1 kilo',
            'category': 'brood',
            'image': 'plaatje',
            'deal': '€1 korting',
            'price': '1.99',
            'dateStart': '2022-04-11',
            'dateEnd': '2022-04-18',
            'link': 'linkje',
            'shop': 'lidl'
        }, {
            'product': 'Hero jam',
            'productInfo': 'Minder zoet',
            'category': 'beleg',
            'image': 'plaatje',
            'deal': 'op=op',
            'price': '1.49',
            'dateStart': '2022-04-11',
            'dateEnd': '',
            'link': 'linkje',
            'shop': 'lidl'
        }]

        test_offer_object_expected = [{
            'product': 'Luxe stol',
            'productInfo': '1 kilo',
            'category': 'brood',
            'image': 'plaatje',
            'deal': '€1 korting',
            'price': '1.99',
            'dateStart': '2022-04-11',
            'dateEnd': '2022-04-18',
            'link': 'linkje',
            'shop': 'lidl',
            'id': 1
        }, {
            'product': 'Hero jam',
            'productInfo': 'Minder zoet',
            'category': 'beleg',
            'image': 'plaatje',
            'deal': 'op=op',
            'price': '1.49',
            'dateStart': '2022-04-11',
            'dateEnd': '',
            'link': 'linkje',
            'shop': 'lidl',
            'id': 2
        }]

        addId = giveid.give_id_to_offers(test_offer_object)
        self.assertEqual(addId, test_offer_object_expected)

if __name__ == '__main__':
    unittest.main(
        testRunner=xmlrunner.XMLTestRunner(output="."),
        failfast=False,
        buffer=False,
        catchbreak=False,
        verbosity=1)
