import os
 # -*- coding: utf-8 -*-
import unittest

from selenium.webdriver import ActionChains, DesiredCapabilities, Remote
from tests.page_objects.pages import AuthPage, CreatePage, CampaignsPage
from tests.page_objects.Const import Const
def login(driver):
    auth_page = AuthPage(driver)
    auth_page.open()
    auth_form = auth_page.form
    auth_form.set_domain(Const.DOMAIN)
    auth_form.set_login(Const.USERNAME)
    auth_form.set_password(Const.PASSWORD)
    auth_form.submit()
    email = create_page.top_menu.get_email()
    self.assertEqual(Const.USERNAME+Const.DOMAIN, email)


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

    def test_login(self):
        create_page = CreatePage(self.driver)
        create_page.open()
        email = create_page.top_menu.get_email()
        self.assertEqual(Const.USERNAME+Const.DOMAIN, email)

    def test_add_ad(self):
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

    def test_comp_with_gender(self):
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

        create_page.create_comp_button.click()
        comp_page = CampaignsPage(self.driver)
        info = comp_page.edit_last.text
        self.assertEqual(info.split(',')[0], u"Ж")

    def test_date_diff_time(self):
        create_page = CreatePage(self.driver)
        create_page.open()
        time_selector = create_page.time_selector
        time_selector.toogle()
        time_selector.set_time(Const.FROM_DATE, Const.TO_DATE)
        self.assertEqual((int)(time_selector.get_timediff().split(' ')[0]), (int)((Const.TO_DATE - Const.FROM_DATE).days + 1), "Wrong calculation difftiem")

    def test_toogle_date(self):
        create_page = CreatePage(self.driver)
        create_page.open()
        time_selector = create_page.time_selector
        time_selector.toogle()
        time_selector.set_time(Const.FROM_DATE, Const.TO_DATE)
        time_selector.toogle()
        time_selector.toogle()
        self.assertEqual(time_selector.get_begin_time(), Const.FROM_DATE, "From date doesn't match")
        self.assertEqual(time_selector.get_end_time(), Const.TO_DATE, "End date doesn't match")

    def test_wrong_data_order(self):
        create_page = CreatePage(self.driver)
        create_page.open()
        time_selector = create_page.time_selector
        time_selector.toogle()
        time_selector.set_time(Const.TO_DATE, Const.FROM_DATE)
        self.assertEqual(time_selector.get_begin_time(), Const.FROM_DATE, "From date doesn't match")
        self.assertEqual(time_selector.get_end_time(), Const.TO_DATE, "End date doesn't match")

    pass
