
from SeleniumLibrary import SeleniumLibrary as sel
from robot.libraries.BuiltIn import BuiltIn


class Common_copy():

    selib = sel()

    def input_username1(self, username):
        self.selib.input_text("username_field", username)

    def open_browser1(self, url):
        self.selib.open_browser(url)

    def check_text(self):
        webdriver = self.selib.driver
        text = webdriver.find_element_by_xpath("//label[@for = 'username_field']").text
        BuiltIn().log(text)
