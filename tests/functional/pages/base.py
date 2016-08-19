# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pypom import Page, Region


class BasePage(Page):

    URL_TEMPLATE = '/{locale}'

    def __init__(self, selenium, base_url, locale='en-US', **url_kwargs):
        super(BasePage, self).__init__(selenium, base_url, locale=locale, **url_kwargs)

    def wait_for_page_to_load(self):
        self.wait.until(lambda s: self.seed_url in s.current_url)
        el = self.find_element(By.TAG_NAME, 'html')
        self.wait.until(lambda s: 'loaded' in el.get_attribute('class'))
        return self

    @property
    def navigation(self):
        return self.Navigation(self)
"""
    @property
    def footer(self):
        return self.Footer(self)
"""
    class Navigation(Region):

        _root_locator = (By.ID, 'main-nav')
        _toggle_locator = (By.CSS_SELECTOR, '> ul > li:first-child > a:first-child')
        _menu_locator = (By.ID, 'nav-platform-submenu')

        def show(self):
            assert not self.is_displayed, 'Menu is already displayed'
            self.find_element(*self._toggle_locator).click()
            self.wait.until(lambda s: self.is_displayed)
            return self

        @property
        def is_displayed(self):
            toggle = self.find_element(*self._toggle_locator)
            return (self.find_element(*self._menu_locator).is_displayed() and
                toggle.get_attribute('aria-expanded') == 'true')
"""
        def open_about(self):
            self.find_element(*self._about_locator).click()
            from about import AboutPage
            return AboutPage(self.selenium, self.page.base_url).wait_for_page_to_load()

        def open_participate(self):
            self.find_element(*self._participate_locator).click()
            from contribute.contribute import ContributePage
            return ContributePage(self.selenium, self.page.base_url).wait_for_page_to_load()

        def open_firefox(self):
            self.find_element(*self._firefox_locator).click()
            from firefox.products import ProductsPage
            return ProductsPage(self.selenium, self.page.base_url).wait_for_page_to_load()

    class Footer(Region):

        _root_locator = (By.ID, 'main-footer')
        _language_locator = (By.ID, 'language')

        @property
        def language(self):
            select = self.find_element(*self._language_locator)
            option = select.find_element(By.CSS_SELECTOR, 'option[selected]')
            return option.get_attribute('value')

        @property
        def languages(self):
            el = self.find_element(*self._language_locator)
            return [o.get_attribute('value') for o in Select(el).options]

        def select_language(self, value):
            el = self.find_element(*self._language_locator)
            Select(el).select_by_value(value)
            self.wait.until(lambda s: '/{0}/'.format(value) in s.current_url)
"""
