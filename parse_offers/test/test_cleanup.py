import unittest

from cleanup import categorize

class TestCleanup(unittest.TestCase):

    def test_return_category(self):
        resultingCategory = categorize.findCategoryForProduct("bier", "bier")
        self.assertTrue(resultingCategory == 'bier')

if __name__ == '__main__':
    unittest.main()
