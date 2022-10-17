import unittest
import xmlrunner
from cleanup import categorize, cleantext, cleandate, giveid, cleandeal

class TestCleanup(unittest.TestCase):
    """
    Testen van de cleanup module
    """

    def test_return_category_but_ignore_words(self):
        """
        ✅ Categorie voor product vinden maar ook woorden negeren 👉
        """
        resulting_category = categorize.find_category("een biefstuk", "bla bla")
        self.assertTrue(resulting_category == 'vlees')

        resulting_category = categorize.find_category("een vegan", "bla bla")
        self.assertTrue(resulting_category == 'vegan')

        resulting_category = categorize.find_category("een vegan biefstuk", "bla bla")
        self.assertTrue(resulting_category == 'vegan')

        resulting_category = categorize.find_category("een biefstuk vegan", "bla bla")
        self.assertTrue(resulting_category == 'vegan')

        resulting_category = categorize.find_category("een biefstuk vegan biefstuk", "bla bla")
        self.assertTrue(resulting_category == 'vegan')

        resulting_category = categorize.find_category("calvé saus", "bla bla")
        self.assertTrue(resulting_category != 'beleg')

    def test_return_category_none_found(self):
        resulting_category = categorize.find_category("derpie derp", "")
        self.assertTrue(resulting_category == 'geen-categorie')

        resulting_category = categorize.find_category("", "derpie derp")
        self.assertTrue(resulting_category == 'geen-categorie')

        resulting_category = categorize.find_category("", "")
        self.assertTrue(resulting_category == 'geen-categorie')

    def test_return_category_by_title(self):
        """
        ✅ Categorie voor product wordt gevonden in titel 👉
        """
        resulting_category = categorize.find_category("bier water", "een flesje")
        self.assertTrue(resulting_category == 'bier')

    def test_return_category_by_description(self):
        """
        ✅ Categorie voor product wordt gevonden in beschrijving 👉
        """
        resulting_category = categorize.find_category("een flesje", "water bier")
        self.assertTrue(resulting_category == 'bier')

    def test_return_category_w_empty_title(self):
        """
        ✅ Categorie voor product wordt gevonden met ontbrekende titel 👉
        """
        resulting_category = categorize.find_category("", "bier")
        self.assertTrue(resulting_category == 'bier')

    def test_return_category_w_empty_description(self):
        """
        ✅ Categorie voor product wordt gevonden met ontbrekende beschrijving 👉
        """
        resulting_category = categorize.find_category("bier", "")
        self.assertTrue(resulting_category == 'bier')

    def test_return_single_word_capitalized(self):
        """
        ✅ Categorie voor product wordt gevonden met enkel woord en hoofdletter 👉
        """
        resulting_category = categorize.find_category("Lenor", "derp derp")
        self.assertTrue(resulting_category == 'huishouden')

    def test_return_single_word_w_apostrof(self):
        """
        ✅ Categorie voor product wordt gevonden met enkel woord en apostrof 👉
        """
        resulting_category = categorize.find_category("Mango's Ready to Eat", "2-pack")
        self.assertTrue(resulting_category == 'fruit')

    def test_return_category_found_by_multiple_keyword_string(self):
        """
        ✅ Categorie voor product wordt gevonden op basis van meerdere woorden in een string 👉
        """
        resulting_category = categorize.find_category("Een friesche vlag latte pak", "2-pack")
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

    def test_clean_date(self):
        """
            ✅ Definitions from cleandate module return results 👉
        """
        expected_date_string = "2017-01-01"
        created_date_string = cleandate.return_full_datestring("2017", "01", "01")
        self.assertTrue(created_date_string == expected_date_string)

        expected_month_index = "02"
        created_month_index = cleandate.return_index_by_full_month_text("februari")

        self.assertTrue(created_month_index == expected_month_index)

        expected_weekday = "maandag"
        created_weekday_string = cleandate.return_weekday_string("2022-10-17")
        self.assertTrue(created_weekday_string == expected_weekday)

        expected_future_date_string = "2023-01-02"
        created_future_date = cleandate.return_calculated_date("2022-12-31", 2)
        self.assertTrue(created_future_date == expected_future_date_string)
        
        expected_sunday_day = "2022-10-23"
        created_first_sunday = cleandate.return_first_sunday_startdate_string("2022-10-18")
        self.assertTrue(created_first_sunday == expected_sunday_day)

    def test_clean_deal(self):
        """
            ✅ Definitions from cleandeal module return results 👉
        """       
        expected_deal = "50"
        calculated_deal = cleandeal.calculate_percentage("15.00", "7.50")
        self.assertTrue(calculated_deal == expected_deal)

if __name__ == '__main__':
    unittest.main(
        testRunner=xmlrunner.XMLTestRunner(output="."),
        failfast=False,
        buffer=False,
        catchbreak=False,
        verbosity=1)
