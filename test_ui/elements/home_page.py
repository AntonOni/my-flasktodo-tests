import selenium
from selenium.webdriver.common.by import By
import time


class HomePage:
    def __init__(self, chrome):
        self.chrome = chrome
        self.create_btn_selector = "body > div > a"
        self.edit_btn_selector = "#edit"
        self.delete_btn_selector = "#delete"
        self.show_task_btn_selector = "#show"


        self.delete_btn_class = "btn btn-danger"
        self.show_btn_class = "btn btn-info"
        self.main_title_xpath = "/html/body/div/div[1]/h1"


        self.paginate_button = "paginate_button "
        self.table_ids = "sorting_1"
        self.first_table_row = "/html/body/div/div[2]/table/tbody/tr[1]/td[3]"


    def get_main_title_text(self):
        title_text = self.chrome.find_element_by_xpath(self.main_title_xpath)
        return title_text.get_attribute('innerText')

    def click_create(self):
        create_page = self.chrome.find_element_by_css_selector(self.create_btn_selector)
        create_page.click()

    def find_paginate_buttons(self):
        paginate_buttons = self.chrome.find_elements_by_class_name(self.paginate_button)
        return paginate_buttons

    def click_paginate_button(self, paginate_button):
        paginate_button.click()

    def find_all_table_ids(self):
        all_table_ids = self.chrome.find_elements_by_class_name(self.table_ids)
        return all_table_ids

    def click_edit(self):
        edit_page = self.chrome.find_element_by_css_selector(self.edit_btn_selector)
        edit_page.click()

    def find_first_table_row(self):
        first_table_row = self.chrome.find_element_by_xpath(self.first_table_row)
        return first_table_row

    def click_delete(self):
        delete_page = self.chrome.find_element_by_css_selector(self.delete_btn_selector)
        delete_page.click()

    def accept_alert(self):
        alert = self.chrome.switch_to.alert
        alert.accept()

    def click_show_task_btn(self):
        show_task = self.chrome.find_element_by_css_selector(self.show_task_btn_selector)
        show_task.click()



