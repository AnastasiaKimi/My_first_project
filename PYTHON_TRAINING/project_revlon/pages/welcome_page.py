import click


class WelcomePage():

    def __init__(self, page)
        self.page = page

    def search_for_item(self):
        print ("trying to search for item")
        search_icon = self.page.locator("[class='site-nav__link site-nav__link--icon search js-search-header']")
        search_icon.click()
        search_menu = self.page.locator ("[class='icon icon-search']")
        search_menu.fill("Lipstick")



    def click_on_close_popup(self): \
            self.page.locator("[class='needsclick.klaviyo-close-form.go2324193863.kl-private-reset-css-Xuajs1']").click()




