import unittest
import sys
sys.path.append('../src/')

from utils import get_web_content

class TestGetWebDriver(unittest.TestCase):
    
    def test_return_content(self):
        url = 'https://www.google.com.br/'
        result = get_web_content(url)
        self.assertTrue(result)

if __name__ == "__main__":
    unittest.main()