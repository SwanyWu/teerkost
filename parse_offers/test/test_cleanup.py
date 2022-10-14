import unittest
import xmlrunner
from cleanup import categorize, cleantext, giveid

class test_cleanup(unittest.TestCase):

    def test_return_category_but_ignore_words(self):
        """
        ✅ Categorie voor product vinden maar ook woorden negeren 👉 
        """
        resultingCategory = categorize.find_category_for_product("een biefstuk", "bla bla")
        self.assertTrue(resultingCategory == 'vlees')

        resultingCategory = categorize.find_category_for_product("een vegan", "bla bla")
        self.assertTrue(resultingCategory == 'vegan')

        resultingCategory = categorize.find_category_for_product("een vegan biefstuk", "bla bla")
        self.assertTrue(resultingCategory == 'vegan')

        resultingCategory = categorize.find_category_for_product("een biefstuk vegan", "bla bla")
        self.assertTrue(resultingCategory == 'vegan')

        resultingCategory = categorize.find_category_for_product("een biefstuk vegan biefstuk", "bla bla")
        self.assertTrue(resultingCategory == 'vegan')

        resultingCategory = categorize.find_category_for_product("calvé saus", "bla bla")
        self.assertTrue(resultingCategory != 'beleg')

    def test_return_category_none_found(self):
        resultingCategory = categorize.find_category_for_product("derpie derp", "")
        self.assertTrue(resultingCategory == 'geen-categorie')

        resultingCategory = categorize.find_category_for_product("", "derpie derp")
        self.assertTrue(resultingCategory == 'geen-categorie')

        resultingCategory = categorize.find_category_for_product("", "")
        self.assertTrue(resultingCategory == 'geen-categorie')

    def test_return_category_by_title(self):
        """
        ✅ Categorie voor product wordt gevonden in titel 👉 
        """
        resultingCategory = categorize.find_category_for_product("bier water", "een flesje")
        self.assertTrue(resultingCategory == 'bier')

    def test_return_category_by_description(self):
        """
        ✅ Categorie voor product wordt gevonden in beschrijving 👉 
        """
        resultingCategory = categorize.find_category_for_product("een flesje", "water bier")
        self.assertTrue(resultingCategory == 'bier')

    def test_return_category_w_empty_title(self):
        """
        ✅ Categorie voor product wordt gevonden met ontbrekende titel 👉 
        """
        resultingCategory = categorize.find_category_for_product("", "bier")
        self.assertTrue(resultingCategory == 'bier')    
    
    def test_return_category_w_empty_description(self):
        """
        ✅ Categorie voor product wordt gevonden met ontbrekende beschrijving 👉 
        """
        resultingCategory = categorize.find_category_for_product("bier", "")
        self.assertTrue(resultingCategory == 'bier')   

    def test_return_single_word_capitalized(self):
        """
        ✅ Categorie voor product wordt gevonden met enkel woord en hoofdletter 👉 
        """        
        resultingCategory = categorize.find_category_for_product("Lenor", "derp derp")
        self.assertTrue(resultingCategory == 'huishouden')

    def test_return_single_word_w_apostrof(self):
        """
        ✅ Categorie voor product wordt gevonden met enkel woord en apostrof 👉 
        """        
        resultingCategory = categorize.find_category_for_product("Mango's Ready to Eat", "2-pack")
        self.assertTrue(resultingCategory == 'fruit')    

    def test_return_category_found_by_multiple_keyword_string(self):
        """
        ✅ Categorie voor product wordt gevonden op basis van meerdere woorden in een string 👉 
        """                
        resultingCategory = categorize.find_category_for_product("Een friesche vlag latte pak", "2-pack")
        self.assertTrue(resultingCategory == 'zuivel')    

    def test_clean_title(self):
        """
        ✅ Titel van een product is netjes 👉 
        """
        cleanTitle = cleantext.clean_up_title("Jumbo Alle AH bananen* met schil ")
        expectedTitle = "Bananen met schil"
        self.assertEqual(cleanTitle, expectedTitle)

    def test_clean_info(self):
        """
        ✅ Productinfo van een product is netjes 👉 
        """
        cleanInfoText = cleantext.clean_up_info("Alle soorten 300 gram")
        expectedInfoText = "300 gram"
        self.assertEqual(cleanInfoText, expectedInfoText)    

        cleanInfoText = cleantext.clean_up_info("Bijv. de groene soort")
        expectedInfoText = ""
        self.assertEqual(cleanInfoText, expectedInfoText)    

    def test_give_id(self):
        """
        ✅ Product van een eigen ID voorzien 👉 
        """
        testOfferObject = [{
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

        testOfferObjectExpected = [{
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

        addId = giveid.give_id_to_offers(testOfferObject)
        self.assertEqual(addId, testOfferObjectExpected)        

if __name__ == '__main__':
   unittest.main(
        testRunner=xmlrunner.XMLTestRunner(output="."),
        failfast=False,
        buffer=False,
        catchbreak=False,
        verbosity=1)
