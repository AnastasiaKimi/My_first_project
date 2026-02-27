

class WelcomePage:

    def __init__(self, page):
        self.page = page

    def search_for_item(self, item_name="Lipstick"):

        print("trying to search for item")
        self.page.get_by_role("button", name="Search").first.click()
        search_input = self.page.locator("input[type='search']")
        search_input.fill(item_name)
        self.page.keyboard.press("Enter")

    def close_popup_if_exists(self):
        close_button = self.page.get_by_role("button", name="Close dialog")

        if close_button.count() > 0:
            close_button.first.click()



    def go_to_contact_us(self):
        self.page.get_by_role("link", name="Contact Us").click()



    def accept_cookies_if_exists(self):
        accept_button = self.page.locator("#shopify-pc__banner__btn-accept")

        if accept_button.is_visible(timeout=3000):
            accept_button.click()



    def go_to_mascara_collection(self):
        self.page.get_by_role("link", name="Makeup").hover()
        mascara_link = self.page.locator("#x-menu_makeup").locator(
            'a[href="/collections/mascara"]'
        )
        mascara_link.click()

    def go_to_repair_serum(self):
        self.page.goto(
            "https://www.gadecosmetics.com/collections/repair-serum",
            wait_until="domcontentloaded")

    def wait_for_cart_drawer_open(self):
        self.cart_drawer.wait_for()




