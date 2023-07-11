
class MyReportsPageLocators:
    """
    تمام المنت های مربوط به my reports در این کلاس قرار دارد
    """
    def __init__(self):
        self.locators = {
            # "assert_my_reports_label": '//*[@text="My Reports"]',
            "my_reports_list": 'com.dariaos.reporter:id/rv_apps_fragment_reports_list',
            "assert_report_type_label": 'com.dariaos.reporter:id/txt_report_type_report_row',
            "message_button": 'com.dariaos.reporter:id/img_message_report_row',
            "message_label": 'android:id/alertTitle',

        }

    def __getitem__(self, index):
        return self.locators[index]