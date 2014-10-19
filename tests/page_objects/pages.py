__author__ = 'mike'
import urlparse
from tests.page_objects.comp import AuthForm, TopMenu, Slider, TimeSelector, BaseCampaignSettings, AdsForm, Gender
from selenium.webdriver.support.wait import WebDriverWait

class Page(object):
    BASE_URL = 'https://target.mail.ru'
    PATH = ''

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        url = urlparse.urljoin(self.BASE_URL, self.PATH)
        self.driver.get(url)


class AuthPage(Page):
    PATH = '/login'

    @property
    def form(self):
        return AuthForm(self.driver)


class CreatePage(Page):
    PATH = '/ads/create'
    CREATE = '.main-button-new'

    @property
    def top_menu(self):
        return TopMenu(self.driver)

    @property
    def slider(self):
        return Slider(self.driver)

    @property
    def base_settings(self):
        return BaseCampaignSettings(self.driver)

    @property
    def ads_form(self):
        return AdsForm(self.driver)

    @property
    def gender(self):
        return Gender(self.driver)

    @property
    def create_comp_button(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.CREATE)
        )

    @property
    def time_selector(self):
        return TimeSelector(self.driver)


class CampaignsPage(Page):
    PATH = '/ads/campaigns/'
    LAST_EDIT = '.campaign-title__settings .js-campaign-title-settings'

    @property
    def edit_last(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_class_name('campaign-title__settings')
        )

    @property
    def gender_info(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector('.campaign-settings-list__targeting__value.js-campaign-settings-value')
        )