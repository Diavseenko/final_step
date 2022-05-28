class BasePage():
    def  __int__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self, browser, url):
        return self.browser.get(self.url)
