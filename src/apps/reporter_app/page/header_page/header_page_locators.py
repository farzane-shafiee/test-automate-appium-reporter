
class HeaderPageLocators:
    """
    تمام المنت های مربوط به سرصفحه در این کلاس قرار دارد
    """
    def __init__(self):
        self.locators = {
            "search_button": 'com.dariaos.reporter:id/search_button',
            "search_input": 'com.dariaos.reporter:id/search_src_text',
            "assert_element_clock": '//*[@text="Clock"]',
            "report_button": 'com.dariaos.reporter:id/btn_report_app_row',

        }

    def __getitem__(self, index):
        return self.locators[index]