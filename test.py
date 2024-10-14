from atf import *
from atf.ui import *
from pages.auth_page import AuthPage
from pages.dialog_page import MainPage, Chats, PanelMoveDialog, ControlPanel


class Test(TestCaseUI):
    message = 'Сообщение'

    @classmethod
    def setUpClass(cls):
        AuthPage(cls.driver).auth()
        cls.main = MainPage(cls.driver)
        cls.chats = Chats(cls.driver)
        cls.move_panel = PanelMoveDialog(cls.driver)
        cls.control_panel = ControlPanel(cls.driver)

    def setUp(self):
        self.main.check_load()

    def tearDown(self):
        self.browser.close_windows_and_alert()

    def test_01_move_message(self):
        """Перемещение сообщения в папку"""

        folder_to_move = 'папка для перемещения'
        text_message = self.main.diaologs.item(contains_text=self.message).should_be(Displayed).text

        self.main.diaologs.item(contains_text=text_message).select_menu_actions("Переместить")
        self.move_panel.check_load()
        self.move_panel.move_dialog.row(contains_text=folder_to_move).click()
        self.move_panel.move_dialog.should_not_be(Displayed)

        folder = self.main.folders.row(contains_text=folder_to_move)
        folder.click()
        self.main.marker_folders.should_be(Displayed)
        self.main.diaologs.item(with_text=text_message).should_be(Displayed)
        self.main.count_folder.should_be(ExactText('1'))

        self.main.diaologs.item(contains_text=text_message).select_menu_actions("Переместить")
        self.move_panel.check_load()
        self.move_panel.move_dialog.row(contains_text="Все сообщения").element('div').click()
        self.move_panel.move_dialog.should_not_be(Displayed)
        self.main.diaologs.should_be(CountElements(0))

    def test_02_check_date(self):
        """Проверка даты сообщения"""

        date_message = self.main.date_message.text
        self.main.tabs.select("Чаты")
        self.main.marker_tabs.should_be(Displayed)
        self.chats.chats.item(contains_text=self.message).should_be(Displayed)
        self.chats.date_message.should_be(ExactText(date_message))

    def test_03_select_tag(self):
        """Пометить сообщение тегом"""
        test = 'Тест'
        message = self.main.diaologs.item(contains_text=self.message)
        message.select_menu_actions("Пометить")
        self.control_panel.panel.check_load()
        self.control_panel.panel.item(contains_text=test).click()
        self.control_panel.panel.should_not_be(Displayed)

        self.main.count_tag.should_be(ExactText('1'))
        message.should_be(ContainsText(test))

        message.select_menu_actions("Пометить")
        self.control_panel.panel.check_load()
        self.control_panel.panel.item(contains_text=test).click()
        self.control_panel.panel.should_not_be(Displayed)
        message.should_not_be(ContainsText(test))


