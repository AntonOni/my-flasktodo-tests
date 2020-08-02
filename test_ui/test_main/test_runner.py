# -*- coding: utf-8 -*-
import pytest
from elements.home_page import HomePage
from elements.create_edit_page import CreateEditPage
import time
from selenium.webdriver.support.ui import WebDriverWait
from elements.show_task import ShowTask


@pytest.mark.usefixtures("driver_setup")
class TestToDo:
    last_element_before_creating = ""
    last_element_after_creating = ""


    def test_ind(self):
        print("Start test 1")
        home_page = HomePage(self.chrome)
        title_text = home_page.get_main_title_text()
        assert title_text == "To Do List"

    def test_create_element(self):
        print("Start test 2")
        # Берем последний элемент до добавления
        home_page = HomePage(self.chrome)
        time.sleep(5)
        paginate_buttons = home_page.find_paginate_buttons()
        if len(paginate_buttons) > 1:
            paginate_buttons[-2].click()
            time.sleep(3)
            rows = self.chrome.find_elements_by_tag_name("tr")
            self.last_element_before_creating = rows[-1].text

        # Добавляем новый елемент.
        home_page.click_create()
        create_page = CreateEditPage(self.chrome)
        time.sleep(2)
        create_page.fill_task_name()
        time.sleep(2)
        create_page.fill_descreption()
        time.sleep(2)
        create_page.click_submit_btn()
        time.sleep(2)
        create_page.close_alert()

        # Берем последний элемент после добавления и сравниваем ID элементов до добавления и после
        time.sleep(5)
        paginate_buttons = home_page.find_paginate_buttons()
        if len(paginate_buttons) > 1:
            paginate_buttons[-2].click()
            time.sleep(3)
            rows = self.chrome.find_elements_by_tag_name("tr")
            self.last_element_after_creating = rows[-1].text
            id_before_creating = self.last_element_before_creating.split(" ")
            if id_before_creating:
                id_before_creating = int(id_before_creating[0])
            id_after_creating = self.last_element_after_creating.split(" ")
            if id_after_creating:
                id_after_creating = int(id_after_creating[0])
            assert (id_before_creating+1) == id_after_creating

    def test_edit_element(self):
        print("Start test 3")
        home_page = HomePage(self.chrome)
        time.sleep(5)
        paginate_buttons = home_page.find_paginate_buttons()
        if len(paginate_buttons) > 1:
            paginate_buttons[1].click()
            time.sleep(3)

        all_table_ids = home_page.find_all_table_ids()
        if len(all_table_ids) > 0:
            first_table_id = all_table_ids[0]
            first_table_id.click()
            home_page.click_edit()
            create_page = CreateEditPage(self.chrome)
            time.sleep(2)
            create_page.fill_task_name(edited=" new_one")
            time.sleep(2)
            create_page.fill_descreption(edited=" new_one")
            time.sleep(2)
            create_page.click_submit_btn()
            time.sleep(2)
            create_page.close_alert()
            first_table_row = home_page.find_first_table_row()
            time.sleep(5)
            if first_table_row:
                first_table_row_text = first_table_row.get_attribute("innerHTML")
                print(first_table_row_text)
                assert " new_one" in first_table_row_text


    def test_delete_element(self):
        print("Start test 4")
        fifth_table_id_before = None
        fifth_table_id_after = None

        home_page = HomePage(self.chrome)
        all_table_ids = home_page.find_all_table_ids()
        if len(all_table_ids) > 0:
            fifth_table_id_before = all_table_ids[4].text

        all_table_ids = home_page.find_all_table_ids()
        if len(all_table_ids) > 0:
            fifth_table_id = all_table_ids[4]
            fifth_table_id.click()
            time.sleep(3)
            home_page.click_delete()
            time.sleep(3)

            home_page.accept_alert()

        new_all_table_ids = home_page.find_all_table_ids()
        if len(new_all_table_ids) > 0:
            fifth_table_id_after = new_all_table_ids[4].text

        assert not fifth_table_id_before == fifth_table_id_after

    def test_show_task(self):
        print("Start test 5")
        ninth_table_id_before = None

        home_page = HomePage(self.chrome)
        all_table_ids = home_page.find_all_table_ids()
        if len(all_table_ids) > 0:
            ninth_table_id_before = all_table_ids[8].text
            all_table_ids[8].click()

        home_page.click_show_task_btn()
        time.sleep(2)
        show_task_page = ShowTask(self.chrome)
        title_id = show_task_page.get_title_id()
        assert title_id == ninth_table_id_before




