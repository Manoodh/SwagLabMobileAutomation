# Inside config/settings.py
import os

class MobileConfig:
    APP_PATH = "D:/Code/Apps/mda-2.2.0-25.apk"
    
    CAPABILITIES = {
        "platformName": "Android",
        "automationName": "UiAutomator2",
        "deviceName": "AndroidPhone",
        "app": APP_PATH,
        "noReset": False,
        "ensureWebviewsHavePages": True,
        "nativeWebScreenshot": True,
        
        # Public package router configuration
        "appPackage": "com.saucelabs.mydemoapp.android",
        "appWaitActivity": "com.saucelabs.mydemoapp.android.view.activities.SplashActivity, com.saucelabs.mydemoapp.android.view.activities.MainActivity",
        "appWaitDuration": 30000              
    }
    
    APPIUM_SERVER_URL = "http://localhost:4723"