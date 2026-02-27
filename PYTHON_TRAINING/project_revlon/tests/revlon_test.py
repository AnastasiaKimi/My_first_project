from PYTHON_TRAINING.project_revlon.pages.welcome_page import WelcomePage


# class TestRevlonTest():
#     def test_search_item_test(self, setup_playwright_revlon):
#         page=setup_playwright_revlon
#         page.goto("http://www.revlon.com")

class TestRevlonTest():

    def test_search_for_item_and_getting_results(self,setup_playwright_revlon):
        page = setup_playwright_revlon
        result_page = ResultsPage(page)
        welcome_page = WelcomePage(page)
        page.goto("http://www.revlon.com")
        welcome_page.search_for_item()
        welcome_page.click_on_close_popup()


        # result_page.get_text_from_results()


