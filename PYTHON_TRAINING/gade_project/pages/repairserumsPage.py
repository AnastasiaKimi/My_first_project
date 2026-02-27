

class RepairSerumsPage:

    def __init__(self, page):
        self.page = page

    def open_seedology(self):
        self.page.locator(
            "a[href*='seedology-energizing-booster-serum']"
        ).first.click()


