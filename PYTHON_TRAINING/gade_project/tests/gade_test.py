import playwright
from playwright.sync_api import expect

from PYTHON_TRAINING.gade_project.pages.collectionPage import CollectionPage
from PYTHON_TRAINING.gade_project.pages.headerPage import HeaderPage
from PYTHON_TRAINING.gade_project.pages.welcomePage import WelcomePage
from PYTHON_TRAINING.gade_project.pages.productPage import ProductPage
from PYTHON_TRAINING.gade_project.pages.repairserumsPage import RepairSerumsPage


class TestGadeTest:


    def test_search_for_item_and_getting_results(self, setup_playwright_gade_project):
        page = setup_playwright_gade_project
        page.goto("https://www.gadecosmetics.com/")
        welcome_page = WelcomePage(page)
        welcome_page.accept_cookies_if_exists()
        welcome_page.search_for_item()
        page.wait_for_selector(".product-card--root")
        assert page.locator(".product-card--root").count() > 0

    def test_go_to_contact_page(self, setup_playwright_gade_project):
        page = setup_playwright_gade_project
        page.goto("https://www.gadecosmetics.com/")
        welcome_page = WelcomePage(page)
        welcome_page.close_popup_if_exists()
        welcome_page.accept_cookies_if_exists()
        welcome_page.go_to_contact_us()
        assert "contact-us" in page.url

    def test_go_to_mascara_page(self, setup_playwright_gade_project):
        page = setup_playwright_gade_project
        page.goto("https://www.gadecosmetics.com/")
        welcome_page = WelcomePage(page)
        welcome_page.accept_cookies_if_exists()
        welcome_page.go_to_mascara_collection()
        page.wait_for_url("**/collections/mascara")
        assert "mascara" in page.url.lower()



    def test_add_seedology_to_cart(self, setup_playwright_gade_project):
        page = setup_playwright_gade_project
        page.goto("https://www.gadecosmetics.com/cart/clear")
        page.wait_for_load_state("domcontentloaded")
        page.goto("https://www.gadecosmetics.com/", wait_until="domcontentloaded")
        welcome_page = WelcomePage(page)
        welcome_page.accept_cookies_if_exists()
        welcome_page.close_popup_if_exists()
        welcome_page.go_to_repair_serum()
        repair_page = RepairSerumsPage(page)
        repair_page.open_seedology()
        page.wait_for_url("**/seedology-energizing-booster-serum")
        product_page = ProductPage(page)
        product_page.add_to_cart()
        page.goto("https://www.gadecosmetics.com/cart")
        page.wait_for_load_state("domcontentloaded")
        cart_items = page.locator("input[name='updates[]']")
        assert page.locator(
            "a[href*='seedology-energizing-booster-serum']"
        ).count() > 0


    def test_filter_primer_under_40(self, setup_playwright_gade_project):
        page = setup_playwright_gade_project

        page.goto("https://www.gadecosmetics.com/collections/primer",
            wait_until="domcontentloaded")
        welcome_page = WelcomePage(page)
        welcome_page.accept_cookies_if_exists()
        welcome_page.close_popup_if_exists()
        collection_page = CollectionPage(page)
        collection_page.filter_price_under_40()
        collection_page.verify_only_one_product_displayed()
        collection_page.verify_longevity_product()
        page.wait_for_timeout(10000)



    def test_logo_redirects_to_home(self, setup_playwright_gade_project):
        page = setup_playwright_gade_project
        page.goto("https://www.gadecosmetics.com/collections/primer",
            wait_until="domcontentloaded")
        header = HeaderPage(page)
        header.click_logo()
        header.verify_homepage()














