
from playwright.sync_api import expect


class HeaderPage:

    def __init__(self, page):
        self.page = page
        self.logo = page.locator("a[title='GA-DE Cosmetics']")

    def click_logo(self):
        self.logo.click()

    def verify_homepage(self):
        expect(self.page).to_have_url("https://www.gadecosmetics.com/")