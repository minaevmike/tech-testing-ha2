import os

import unittest


from selenium.webdriver import ActionChains, DesiredCapabilities, Remote
from selenium.webdriver.support.ui import Select, WebDriverWait
from tests.page_objects.pages import AuthPage, CreatePage

class Const:
    GAME = 'http://odnoklassniki.ru/game/piratetreasures'
    IMG_PATH = os.path.abspath('img.jpg')
    TITLE = "GABEN GAME"
    TEXT = "GABEN"
    NAME = "GABEN COMP"
    USERNAME = 'tech-testing-ha2-20'
    PASSWORD = os.environ['TTHA2PASSWORD']
    DOMAIN = '@bk.ru'


def login(driver):
    auth_page = AuthPage(driver)
    auth_page.open()
    auth_form = auth_page.form
    auth_form.set_domain(Const.DOMAIN)
    auth_form.set_login(Const.USERNAME)
    auth_form.set_password(Const.PASSWORD)
    auth_form.submit()


class SeleniumTests(unittest.TestCase):
    def setUp(self):
        browser = os.environ.get('TTHA2BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )
        self.driver.maximize_window()
        login(self.driver)

    def tearDown(self):
        self.driver.quit()


    def testLogin(self):
        create_page = CreatePage(self.driver)
        create_page.open()
        email = create_page.top_menu.get_email()
        self.assertEqual(Const.USERNAME+Const.DOMAIN, email)

    def testAddAd(self):
        create_page = CreatePage(self.driver)
        create_page.open()
        settings = create_page.base_settings
        settings.set_advertising()
        settings.set_playground()
        settings.set_name(Const.NAME)
        ads_add = create_page.ads_form
        ads_add.set_link(Const.GAME)
        ads_add.set_image(Const.IMG_PATH)
        ads_add.set_text(Const.TEXT)
        ads_add.set_title(Const.TITLE)
        ads_add.wait_picture()
        ads_add.submit()

        banner = ads_add.added_banner
        self.assertEqual(Const.TITLE, banner.title.text, "Title differs")
        self.assertEqual(Const.TEXT, banner.text.text, "Text differs")
        self.assertIsNotNone(banner.image.value_of_css_property('background-image'), "No image")


    def compWithGender(self):
        create_page = CreatePage(self.driver)
        create_page.open()
        settings = create_page.base_settings
        settings.set_advertising()
        settings.set_playground()
        settings.set_name(Const.NAME)
        ads_add = create_page.ads_form
        ads_add.set_link(Const.GAME)
        ads_add.set_image(Const.IMG_PATH)
        ads_add.set_text(Const.TEXT)
        ads_add.set_title(Const.TITLE)
        ads_add.wait_picture()
        ads_add.submit()

        gender = create_page.gender
        gender.open_menu()
        gender.setMan()
        assert True

