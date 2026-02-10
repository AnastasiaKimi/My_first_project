class TestAdidasTest:
    def test_search_and_get_prices (self,setup_playwright):
        page = setup_playwright
        page.goto("https://www.reebok.com/")

print("test end")