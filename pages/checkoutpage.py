from appium.webdriver.common.appiumby import AppiumBy
from pages.basepage import BasePage

class CheckoutPage(BasePage):
    fullnameField=(AppiumBy.XPATH,'//android.widget.EditText[@resource-id="com.saucelabs.mydemoapp.android:id/fullNameET"]')
    addressline1Field=(AppiumBy.XPATH,'//android.widget.EditText[@resource-id="com.saucelabs.mydemoapp.android:id/address1ET"]')
    cityField=(AppiumBy.XPATH,'//android.widget.EditText[@resource-id="com.saucelabs.mydemoapp.android:id/cityET"]')
    zipcodeField=(AppiumBy.XPATH,'//android.widget.EditText[@resource-id="com.saucelabs.mydemoapp.android:id/zipET"]')
    countryField=(AppiumBy.XPATH,'//android.widget.EditText[@resource-id="com.saucelabs.mydemoapp.android:id/countryET"]')
    topaymentsButton=(AppiumBy.ACCESSIBILITY_ID,"Saves user info for checkout")

    #payment
    fullnamepaymentField=(AppiumBy.XPATH,'//android.widget.EditText[@resource-id="com.saucelabs.mydemoapp.android:id/nameET"]')
    cardnumberField=(AppiumBy.XPATH,'//android.widget.EditText[@resource-id="com.saucelabs.mydemoapp.android:id/cardNumberET"]')
    expirydatField=(AppiumBy.XPATH,'//android.widget.EditText[@resource-id="com.saucelabs.mydemoapp.android:id/expirationDateET"]')
    securitycodeField=(AppiumBy.XPATH,'//android.widget.EditText[@resource-id="com.saucelabs.mydemoapp.android:id/securityCodeET"]')
    revieworderButton=(AppiumBy.ACCESSIBILITY_ID,"Saves payment info and launches screen to review checkout data")

    placeorderButton=(AppiumBy.ACCESSIBILITY_ID,"Completes the process of checkout")

    checkoutcompleteText=(AppiumBy.XPATH,'//android.widget.TextView[@resource-id="com.saucelabs.mydemoapp.android:id/completeTV"]')

    def fillshippingaddress(self,name,address1,city,zip,country):
        self.fill_mobile_field(self.fullnameField,name)
        self.fill_mobile_field(self.addressline1Field,address1)
        self.fill_mobile_field(self.cityField,city)
        self.fill_mobile_field(self.zipcodeField,zip)
        self.fill_mobile_field(self.countryField,country)

    def navigatetopayment(self):
        self.click_mobile_element(self.topaymentsButton)

    def fillpaymentdetails(self,name,card,expiry,security):
        self.fill_mobile_field(self.fullnamepaymentField,name)
        self.fill_mobile_field(self.cardnumberField,card)
        self.fill_mobile_field(self.expirydatField,expiry)
        self.fill_mobile_field(self.securitycodeField,security)

    def navigatetoplaceorder(self):
        self.click_mobile_element(self.revieworderButton)

    def taponplaceorder(self):
        self.click_mobile_element(self.placeorderButton)

    def ischeckoutsuccess(self):
        return self.get_mobile_text(self.checkoutcompleteText)
