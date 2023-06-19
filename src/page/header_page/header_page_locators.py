
class HeaderPageLocators:
    """
    تمام المنت های مربوط به سرصفحه در این کلاس قرار دارد
    """
    def __init__(self):
        self.locators = {
            "search_button": 'com.dariaos.reporter:id/search_button'

        }

    def __getitem__(self, index):
        return self.locators[index]