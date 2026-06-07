from appium.webdriver.common.appiumby import AppiumBy
from pages.basepage import BasePage

class MyCartsPage(BasePage):
    proceedtocheckoutbutton=(AppiumBy.ACCESSIBILITY_ID,"Confirms products for checkout")

    def clickonproceedtocheckout(self):
        self.click_mobile_element(self.proceedtocheckoutbutton)