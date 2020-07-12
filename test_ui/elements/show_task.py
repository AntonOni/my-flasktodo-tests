

class ShowTask:

    def __init__(self, chrome):
        self.chrome = chrome
        self.title_selector = "body > div > h1"
        self.name_xpath = "/html/body/div/text()[1]"
        self.description_xpath = "/html/body/div/text()[2]"

    def get_title_id(self):
        title = self.chrome.find_element_by_css_selector(self.title_selector)
        full_title = title.text
        title_id = full_title.split(" ")[-1]
        return title_id
