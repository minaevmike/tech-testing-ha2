__author__ = 'mike'
import urlparse
from tests.page_objects.comp import AuthForm, TopMenu, Slider, BaseCampaignSettings, AdsForm, Gender
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