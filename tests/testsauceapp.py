# Inside tests/test_login.py
import pytest
from pages.loginpage import LoginPage
from pages.productspage import ProductsPage
from pages.mycartpage import MyCartsPage
from pages.checkoutpage import CheckoutPage

def test_successful_mobile_login(mobile_driver):
    """
    Verifies that a user with valid credentials can successfully 
    open the side menu, submit the form, and view the product catalog.
    """
    # Initialize the page object with our running driver fixture
    login_page = LoginPage(mobile_driver)
    
    print("\n[STEP] Navigating to the Login screen via Side Menu...")
    login_page.navigate_to_login_screen()
    
    print("[STEP] Entering standard user credentials...")
    # Standard testing credentials recognized by the Sauce Labs app
    login_page.login("bob@example.com", "10203040")  
    
    print("[ASSERT] Verifying 'Products' catalog header has rendered...")
    assert login_page.is_catalog_header_visible() is True, "Catalog header was not visible after login submission!"

def testsuccesfullcheckout(mobile_driver):

    login_page = LoginPage(mobile_driver)
    productpage=ProductsPage(mobile_driver)
    mycartpage=MyCartsPage(mobile_driver)
    checkoutpage=CheckoutPage(mobile_driver)

    login_page.navigate_to_login_screen()
    login_page.login("bob@example.com", "10203040") 

    productpage.addfirstitemtocart()
    productpage.navigatetocart()

    mycartpage.clickonproceedtocheckout()

    checkoutpage.fillshippingaddress("Man","32h house","Kochi","675","India")
    checkoutpage.navigatetopayment()
    checkoutpage.fillpaymentdetails("Man","54775","03/25","564")
    checkoutpage.navigatetoplaceorder()

    checkoutpage.taponplaceorder()

    assert checkoutpage.ischeckoutsuccess()=="Checkout Complete"