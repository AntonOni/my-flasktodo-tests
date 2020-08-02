


class CreateEditPage:

    def __init__(self, chrome):
        self.chrome = chrome
        self.task_name_id = "taskName"
        self.descreption_id = "taskDescription"
        # self.submit_btn_selector = "body > div > form > input"
        # self.submit_btn_class_name = "btn btn-primary"
        self.submit_btn_xpath = "/html/body/div/form/input"
        self.cancel_btn_class = "btn btn-danger"

    def close_alert(self):
        alert = self.chrome.switch_to.alert
        alert.accept()

    def fill_task_name(self, edited=""):
        task_name = self.chrome.find_element_by_id(self.task_name_id)
        task_name.send_keys("Some task here" + edited)

    def fill_descreption(self, edited=""):
        descreption = self.chrome.find_element_by_id(self.descreption_id)
        descreption.send_keys("Some descreption also here" + edited)

    def click_submit_btn(self):
        submit_btn = self.chrome.find_element_by_xpath(self.submit_btn_xpath)
        submit_btn.click()
