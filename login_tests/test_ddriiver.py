import unittest
from Common_copy import Common_copy as page
#from selenium import webdriver

class InputFormsCheck(unittest.TestCase):    

    #Opening browser.
    def test_browser(self):
        page1 = page()
        page1.open_browser1("http://localhost:7272/")
        #page1.open_browser1("http://localhost:7272/")


# This line sets the variable “__name__” to have a value “__main__”.
# If this file is being imported from another module then “__name__” will be set to the other module's name.
if __name__ == "__main__":
    unittest.main()