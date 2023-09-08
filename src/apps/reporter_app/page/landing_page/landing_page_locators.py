
class LandingPageLocators:
    """
    تمام المنت های مربوط به سرصفحه در این کلاس قرار دارد
    """
    def __init__(self):
        self.locators = {
            "report_button": 'com.dariaos.reporter:id/btn_report_app_row',
            "search_result_list": '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.dariaos.reporter:id/rv_apps_fragment_apps_list"]//*',
        }

    def __getitem__(self, index):
        return self.locators[index]