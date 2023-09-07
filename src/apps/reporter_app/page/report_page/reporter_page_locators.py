
class ReporterPageLocators:
    """
    تمام المنت های مربوط به سرصفحه در این کلاس قرار دارد
    """
    def __init__(self):
        self.locators = {
            "report_button": 'com.dariaos.reporter:id/btn_report_app_row',
            "assert_element": '//*[@text="Create Report"]',
            "report_type_dropdown": 'android:id/text1',
            "report_type_list": "//*[@class='android.widget.TextView']",
            "attach_file_button": 'com.dariaos.reporter:id/txt_attach_report_page',
            "assert_file_manager": '//*[@text="Recent"]',
            "image_file": 'com.android.documentsui:id/icon_thumb',
            "assert_not_attach_file": '//*[not(@text="Attach File")]',
            "bug_report_text_input": 'com.dariaos.reporter:id/edtTxtReportPage',
            "send_report_button": 'com.dariaos.reporter:id/btnSendReportReportPage',
            "message_text": 'com.dariaos.reporter:id/alertTitle',
            "close_message_button": 'android:id/button1',
            "assert_attach_file": '//*[@text="Attach File"]',
            "thumb_file": 'com.dariaos.reporter:id/img'
        }

    def __getitem__(self, index):
        return self.locators[index]