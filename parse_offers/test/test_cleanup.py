import unittest
import xmlrunner
from cleanup import categorize, cleantext, giveid

class TestCleanup(unittest.TestCase):

    def test_return_category_but_ignore_words(self):
        """
        ✅ Categorie voor product vinden maar ook woorden negeren 👉 
        """
        resultingCategory = categorize.findCategoryForProduct("een biefstuk", "bla bla")
        self.assertTrue(resultingCategory == 'vlees')

        resultingCategory = categorize.findCategoryForProduct("een vegan", "bla bla")
        self.assertTrue(resultingCategory == 'vegan')

        resultingCategory = categorize.findCategoryForProduct("een vegan biefstuk", "bla bla")
        self.assertTrue(resultingCategory == 'vegan')

        resultingCategory = categorize.findCategoryForProduct("een biefstuk vegan", "bla bla")
        self.assertTrue(resultingCategory == 'vegan')

        resultingCategory = categorize.findCategoryForProduct("een biefstuk vegan biefstuk", "bla bla")
        self.assertTrue(resultingCategory == 'vegan')

        resultingCategory = categorize.findCategoryForProduct("calvé saus", "bla bla")
        self.assertTrue(resultingCategory != 'beleg')

    def test_return_category_none_found(self):
        resultingCategory = categorize.findCategoryForProduct("derpie derp", "")
        self.assertTrue(resultingCategory == 'geen-categorie')

        resultingCategory = categorize.findCategoryForProduct("", "derpie derp")
        self.assertTrue(resultingCategory == 'geen-categorie')

        resultingCategory = categorize.findCategoryForProduct("", "")
        self.assertTrue(resultingCategory == 'geen-categorie')


    def test_return_category_by_title(self):
        """
        ✅ Categorie voor product wordt gevonden in titel 👉 
        """
        resultingCategory = categorize.findCategoryForProduct("bier water", "een flesje")
        self.assertTrue(resultingCategory == 'bier')

    def test_return_category_by_description(self):
        """
        ✅ Categorie voor product wordt gevonden in beschrijving 👉 
        """
        resultingCategory = categorize.findCategoryForProduct("een flesje", "water bier")
        self.assertTrue(resultingCategory == 'bier')

    def test_return_category_w_empty_title(self):
        """
        ✅ Categorie voor product wordt gevonden met ontbrekende titel 👉 
        """
        resultingCategory = categorize.findCategoryForProduct("", "bier")
        self.assertTrue(resultingCategory == 'bier')    
    
    def test_return_category_w_empty_description(self):
        """
        ✅ Categorie voor product wordt gevonden met ontbrekende beschrijving 👉 
        """
        resultingCategory = categorize.findCategoryForProduct("bier", "")
        self.assertTrue(resultingCategory == 'bier')   

    def test_return_single_word_capitalized(self):
        """
        ✅ Categorie voor product wordt gevonden met enkel woord en hoofdletter 👉 
        """        
        resultingCategory = categorize.findCategoryForProduct("Lenor", "derp derp")
        self.assertTrue(resultingCategory == 'huishouden')

    def test_return_single_word_w_apostrof(self):
        """
        ✅ Categorie voor product wordt gevonden met enkel woord en apostrof 👉 
        """        
        resultingCategory = categorize.findCategoryForProduct("Mango's Ready to Eat", "2-pack")
        self.assertTrue(resultingCategory == 'fruit')    

    def test_clean_title(self):
        """
        ✅ Titel van een product is netjes 👉 
        """
        cleanTitle = cleantext.cleanUpTitle("Jumbo Alle AH bananen* met schil ")
        expectedTitle = "Bananen met schil"
        self.assertEqual(cleanTitle, expectedTitle)

    def test_clean_info(self):
        """
        ✅ Productinfo van een product is netjes 👉 
        """
        cleanInfoText = cleantext.cleanUpInfo("Alle soorten 300 gram")
        expectedInfoText = "300 gram"
        self.assertEqual(cleanInfoText, expectedInfoText)    

        cleanInfoText = cleantext.cleanUpInfo("Bijv. de groene soort")
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

        addId = giveid.giveIdToOffers(testOfferObject)
        self.assertEqual(addId, testOfferObjectExpected)        

if __name__ == '__main__':
   unittest.main(
        testRunner=xmlrunner.XMLTestRunner(output="."),
        failfast=False,
        buffer=False,
        catchbreak=False,
        verbosity=1)
