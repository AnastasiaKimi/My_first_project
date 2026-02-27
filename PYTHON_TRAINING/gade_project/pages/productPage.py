

class ProductPage:

    def __init__(self, page):
        self.page = page

    def add_to_cart(self):
        with self.page.expect_response("**/cart/add**"):
            self.page.get_by_role("button", name="Add to cart").click()