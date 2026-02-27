from playwright.sync_api import expect


class CollectionPage:

    def __init__(self, page):
        self.page = page
        self.product_cards = page.locator("[data-product-item]")
        self.prices = page.locator(".money")

    def filter_price_under_40(self):
        self.page.goto(
            "https://www.gadecosmetics.com/collections/primer?filter.v.price.gte=0&filter.v.price.lte=40",
            wait_until="domcontentloaded"
        )

        expect(self.product_cards.first).to_be_visible()

    def verify_only_one_product_displayed(self):
        expect(self.product_cards).to_have_count(1)

    def verify_longevity_product(self):
        product = self.page.locator(
            "div.product-card--root[data-product-item][data-handle='longevity-setting-spray']"
        )

        expect(product).to_be_visible()

        price_text = product.locator(".money").inner_text()
        price_value = float(price_text.replace("$", ""))

        assert price_value <= 40

