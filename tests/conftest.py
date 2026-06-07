# Inside tests/conftest.py
import pytest
from appium import webdriver
from appium.options.common import AppiumOptions
from config.settings import MobileConfig

@pytest.fixture(scope="function")
def mobile_driver():
    """
    Spins up the Appium connection to your phone, installs the app,
    and cleanly tears down the session after your test completes.
    """
    # Dynamically inject capabilities from config/settings.py
    options = AppiumOptions().load_capabilities(MobileConfig.CAPABILITIES)
    
    print("\n[SETUP] Initializing Appium automation server connection...")
    driver = webdriver.Remote(
        command_executor=MobileConfig.APPIUM_SERVER_URL, 
        options=options
    )
    
    yield driver  # This delivers the running app instance to your test script
    
    print("\n[TEARDOWN] Terminating app session and disconnecting from driver...")
    driver.quit()