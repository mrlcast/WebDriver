from selenium import webdriver
from page_objects import PageObject, PageElement

class Google(PageObject):
    search_bar = PageElement(id_ ='lst-ib')
    button_search = PageElement(name='btnK')
    button_lucky = PageElement(name='btnI')
    focus = PageElement(id_='gb')

    def search(self, text):
        self.search_bar.send_keys(text)
        self.focus.click()
        self.button_search.click()

    def lucky_search(self, text):
        self.search_bar.send_keys(text)
        self.focus.click()
        self.button_lucky.click()

browser = webdriver.Chrome()
g = Google(browser, 'http://www.google.com')

g.get('')
#g.search('Universidade Positivo')
g.lucky_search('Pós Graduação Testes de SW da UP')
