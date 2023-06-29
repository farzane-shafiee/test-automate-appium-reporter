
class ReporterPageLocators:
    """
    تمام المنت های مربوط به سرصفحه در این کلاس قرار دارد
    """
    def __init__(self):
        self.locators = {
            "report_button": 'com.dariaos.reporter:id/btn_report_app_row',
            "assert_element": '//*[@text="Create Report"]',
            "report_type_dropdown": 'android:id/text1',
            "bug_report_dropdown_button": '//*[@text="Bug Report"]',
            "attach_file_button": 'com.dariaos.reporter:id/txt_attach_report_page',
            "assert_file_manager": '//*[@text="Recent"]',
            "image_file": 'com.android.documentsui:id/icon_thumb',
            "assert_not_attach_file": '//*[not(@text="Attach file")]',
            "bug_report_text_input": 'com.dariaos.reporter:id/edtTxtReportPage',
            "send_report_button": 'com.dariaos.reporter:id/btnSendReportReportPage'
        }

    def __getitem__(self, index):
        return self.locators[index]