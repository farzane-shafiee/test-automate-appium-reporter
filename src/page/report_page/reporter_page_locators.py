
class ReporterPageLocators:
    """
    تمام المنت های مربوط به سرصفحه در این کلاس قرار دارد
    """
    def __init__(self):
        self.locators = {
            "report_type_dropdown": 'android:id/text1',


        }

    def __getitem__(self, index):
        return self.locators[index]