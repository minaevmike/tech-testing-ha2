__author__ = 'mike'
 # -*- coding: utf-8 -*-
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from datetime import datetime
from tests.page_objects.Const import Const

def web_driver_wait_element(driver, selector):
    return WebDriverWait(driver, 30, 0.1).until(
        lambda d: d.find_element_by_css_selector(selector)
    )


def web_driver_wait_elements(driver, selector):
    return WebDriverWait(driver, 30, 0.1).until(
        lambda d: d.find_elements_by_css_selector(selector)
    )


class Component(object):
    def __init__(self, driver):
        self.driver = driver


class AuthForm(Component):
    LOGIN = '#id_Login'
    PASSWORD = '#id_Password'
    DOMAIN = '#id_Domain'
    SUBMIT = '#gogogo>input'

    def set_login(self, login):
        self.driver.find_element_by_css_selector(self.LOGIN).send_keys(login)

    def set_password(self, pwd):
        self.driver.find_element_by_css_selector(self.PASSWORD).send_keys(pwd)

    def set_domain(self, domain):
        select = self.driver.find_element_by_css_selector(self.DOMAIN)
        Select(select).select_by_visible_text(domain)

    def submit(self):
        self.driver.find_element_by_css_selector(self.SUBMIT).click()


class TopMenu(Component):
    EMAIL = '#PH_user-email'

    def get_email(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.EMAIL).text
        )


class Slider(Component):
    SLIDER = '.price-slider__begunok'

    def move(self, offset):
        element = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.SLIDER)
        )
        ac = ActionChains(self.driver)
        ac.click_and_hold(element).move_by_offset(offset, 0).perform()


class BaseCampaignSettings(Component):
    CAMPAIGN_NAME = '.base-setting__campaign-name__input'
    PLAYGROUND = '#pad-games_odkl_abstract'
    ADVERTISING = '#product-type-5208'

    def __init__(self, driver):
        super(BaseCampaignSettings, self).__init__(driver)
        self.name = web_driver_wait_element(self.driver, self.CAMPAIGN_NAME)
        self.advertising = web_driver_wait_element(self.driver, self.ADVERTISING)

    def set_name(self, str):
        self.name.clear()
        self.name.send_keys(str)

    def set_playground(self):
        web_driver_wait_element(self.driver, self.PLAYGROUND).click()

    def set_advertising(self):
        self.advertising.click()


class AdsForm(Component):
    SAVE_BUTTON = '.banner-form__save-button'
    RESET_BUTTON = '.banner-form__reset'
    IMAGE = 'input[data-name="image"]'
    LINK = 'input[data-name="url"]'
    TITLE = 'input[data-name="title"]'
    TEXT = 'textarea[data-name="text"]'

    @property
    def added_banner(self):
        return BannerPreview(self.driver)

    def set_title(self, title):
        self.title.send_keys(title)

    def set_text(self, text):
        self.text.send_keys(text)

    def set_image(self, path):
        web_driver_wait_element(self.driver, self.IMAGE).send_keys(path)

    def set_link(self, link):
        self.link.send_keys(link)

    @property
    def link(self):
        inputs = web_driver_wait_elements(self.driver, self.LINK)
        for element in inputs:
            if element.is_displayed():
                return element

    @property
    def title(self):
        return web_driver_wait_element(self.driver, self.TITLE)

    @property
    def text(self):
        return web_driver_wait_element(self.driver, self.TEXT)

    def submit(self):
        return self.driver.find_element_by_css_selector(self.SAVE_BUTTON).click()

    def reset(self):
        web_driver_wait_element(self.driver, self.RESET_BUTTON).click()

    def loading_image(self, driver):
        images = driver.find_elements_by_css_selector('.banner-preview .banner-preview__img')
        for image in images:
            if image.value_of_css_property("width") == '90px':
                return WebDriverWait(image, 30, 0.1).until(
                    lambda d: d.value_of_css_property("background-image") is not None)

    def wait_picture(self):
        WebDriverWait(self.driver, 30, 0.1).until(lambda d: self.loading_image(d))


class BannerPreview(Component):
    TITLE = '.added-banner .banner-preview__title'
    IMAGE = '.added-banner .banner-preview__img'
    TEXT = '.added-banner .banner-preview__text'

    @property
    def title(self):
        return web_driver_wait_element(self.driver, self.TITLE)

    @property
    def text(self):
        return web_driver_wait_element(self.driver, self.TEXT)

    @property
    def image(self):
        images = web_driver_wait_elements(self.driver, self.IMAGE)
        for image in images:
            if image.value_of_css_property('background-image') is not None:
                return image

    def get_info(self):
        return self.title.text, self.text.text, self.image.value_of_css_property('background-image')


class Gender(Component):
    TAG = 'campaign-setting__value'
    MAN = '#sex-M'

    def open_menu(self):
        self.driver.find_element_by_class_name(self.TAG).click()

    def setMan(self):
        web_driver_wait_element(self.driver, self.MAN).click()


class TimeSelector(Component):
    FROM_DATE = ".campaign-setting__detail__date-input[data-name=from]"
    TO_DATE = ".campaign-setting__detail__date-input[data-name=to]"
    WHEN = ".all-settings__group[data-name=when]"
    DATE = ".campaign-setting__value.js-setting-value"
    DATES = ".all-settings__item[data-name=date]"
    SETTING = ".create-page__settings"

    def __init__(self, driver):
        super(TimeSelector, self).__init__(driver)
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath("//span[@class='campaign-setting__name'][text() = 'Время работы кампании']")
        )
        web_driver_wait_element(self.driver, self.SETTING)
        self.when = web_driver_wait_element(self.driver, self.WHEN)
        self.dates = self.when.find_element_by_css_selector(self.DATES)
        self.time = self.dates.find_element_by_css_selector(self.DATE)

    def _wait_for_load(self):
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath("//span[@class='campaign-setting__name'][text() = 'Время работы кампании']")
        )
    def toogle(self):
        self._wait_for_load()
        self.time.click()

    def set_time(self, time_begin, time_end):
        self._wait_for_load()
        begin = web_driver_wait_element(self.driver, self.FROM_DATE)
        begin.send_keys(time_begin.strftime('%d.%m.%Y'))
        end = web_driver_wait_element(self.driver, self.TO_DATE)
        end.send_keys(time_end.strftime('%d.%m.%Y'))
        end.send_keys(Keys.RETURN)

    def get_timediff(self):
        self._wait_for_load()
        return self.time.text

    def get_begin_time(self):
        self._wait_for_load()
        return datetime.strptime(web_driver_wait_element(self.driver, self.FROM_DATE).get_attribute('value'), Const.FORMAT)

    def get_end_time(self):
        self._wait_for_load()
        return datetime.strptime(web_driver_wait_element(self.driver, self.TO_DATE).get_attribute('value'), Const.FORMAT)



