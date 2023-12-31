
class MyReportsPageLocators:
    """
    تمام المنت های مربوط به my reports در این کلاس قرار دارد
    """
    def __init__(self):
        self.locators = {
            "assert_my_reports_label": '//*[@text="My Reports"]',
            "my_reports_list": '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.dariaos.reporter:id/rv_apps_fragment_reports_list"]//*',
            "assert_report_type_label": '//android.widget.TextView[@resource-id="com.dariaos.reporter:id/txt_report_type_report_row"]',
            "assert_report_name_label": 'com.dariaos.reporter:id/txt_name_report_row',
            "message_button": 'com.dariaos.reporter:id/img_message_report_row',
            "message_label": 'android:id/alertTitle',
            "date_time_label": 'com.dariaos.reporter:id/txt_report_id_report_row',
            "dialog_text_button": 'com.dariaos.reporter:id/img_message_report_row',
            "dialog_text_frame_layout": 'android:id/content',
            "dialog_text_message": 'android:id/message',
        }

    def __getitem__(self, index):
        return self.locators[index]