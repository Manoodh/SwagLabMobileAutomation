from appium.webdriver.common.appiumby import AppiumBy
from pages.basepage import BasePage

class ProductsPage(BasePage):

    firstproductitem=(AppiumBy.XPATH,'(//android.widget.ImageView[@content-desc="Product Image"])[1]')

    addtocartbutton=(AppiumBy.ACCESSIBILITY_ID,"Tap to add product to cart")

    gotocartbutton=(AppiumBy.ACCESSIBILITY_ID,"Displays number of items in your cart")

    def addfirstitemtocart(self):
        self.click_mobile_element(self.firstproductitem)
        self.click_mobile_element(self.addtocartbutton)

    def navigatetocart(self):
        self.click_mobile_element(self.gotocartbutton)