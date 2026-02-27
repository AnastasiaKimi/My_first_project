class WelcomePage():

    def __init__(self,page):
        self.page = page

    def search_for_item(self):
        print ("trying to search for item")
        search_icon = self.page.locator("[id='header-search']")
        search_icon.click()
        locators = self.page.query_selector_all("[name='q']")
        search_menu = locators[1]
        search_menu.click()
        search_menu.fill("Shirt")


    def click_on_close_popup(self):\
            self.page.locator("[class='spicegems_cr_icon_close_Svg']").click()