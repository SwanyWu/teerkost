import unittest

from cleanup import categorize

class TestCleanup(unittest.TestCase):

    def test_return_category_by_title(self):
        resultingCategory = categorize.findCategoryForProduct("bier water", "een flesje")
        self.assertTrue(resultingCategory == 'bier')

    def test_return_category_by_description(self):
        resultingCategory = categorize.findCategoryForProduct("een flesje", "water bier")
        self.assertTrue(resultingCategory == 'bier')

    def test_return_category_by_title_w_minus(self):
        resultingCategory = categorize.findCategoryForProduct("een flesje", "bier-klein-bier")
        self.assertTrue(resultingCategory == 'bier')

    def test_return_category_by_description_w_minus(self):
        resultingCategory = categorize.findCategoryForProduct("flesje-bier-groot", "een flesje")
        self.assertTrue(resultingCategory == 'bier')

    def test_return_category_w_empty_title(self):
        resultingCategory = categorize.findCategoryForProduct("", "bier")
        self.assertTrue(resultingCategory == 'bier')    
    
    def test_return_category_w_empty_description(self):
        resultingCategory = categorize.findCategoryForProduct("bier", "")
        self.assertTrue(resultingCategory == 'bier')   

    def test_return_empty_w_empty_input(self):
        resultingCategory = categorize.findCategoryForProduct("", "")
        self.assertTrue(resultingCategory == '') 

    def test_return_empty(self):
        resultingCategory = categorize.findCategoryForProduct("niets", "niks")
        self.assertTrue(resultingCategory == '')          

if __name__ == '__main__':
    unittest.main()
