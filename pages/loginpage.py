# Inside pages/login_page.py
from appium.webdriver.common.appiumby import AppiumBy
from pages.basepage import BasePage

class LoginPage(BasePage):
    # --- Mobile Accessibility ID Locators ---
    MENU_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "View menu")
    MENU_LOGIN_OPTION = (AppiumBy.ACCESSIBILITY_ID, "Login Menu Item")
    
    USERNAME_FIELD = (AppiumBy.XPATH, '//android.widget.EditText[@resource-id="com.saucelabs.mydemoapp.android:id/nameET"]')
    PASSWORD_FIELD = (AppiumBy.XPATH, '//android.widget.EditText[@resource-id="com.saucelabs.mydemoapp.android:id/passwordET"]')
    LOGIN_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "Tap to login with given credentials")
    
    # Android specific dynamic text finder to verify successful login screen transition
    CATALOG_HEADER = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Products")')

    # --- Mobile Business Workflows ---
    def navigate_to_login_screen(self):
        """Opens the side navigation drawer and taps the login option"""
        self.click_mobile_element(self.MENU_BUTTON)
        self.click_mobile_element(self.MENU_LOGIN_OPTION)

    def login(self, username, password):
        """Types user credentials and taps the submit button"""
        self.fill_mobile_field(self.USERNAME_FIELD, username)
        self.fill_mobile_field(self.PASSWORD_FIELD, password)
        self.click_mobile_element(self.LOGIN_BUTTON)

    def is_catalog_header_visible(self) -> bool:
        """Checkpoint to confirm the product catalog loaded post-login"""
        return self.wait_for_element(self.CATALOG_HEADER).is_displayed()