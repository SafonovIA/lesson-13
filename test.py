from atf import *
from atf.ui import *
from pages.auth_page import AuthPage
from pages.dialog_page import Dialog, Panel, Folders, Tabs


class Test(TestCaseUI):

    @classmethod
    def setUpClass(cls):
        AuthPage(cls.driver).auth()
        cls.dialog = Dialog(cls.driver)
        cls.panel = Panel(cls.driver)
        cls.folder = Folders(cls.driver)
        cls.tab = Tabs(cls.driver)

    def setUp(self):
        self.dialog.check_load()

    def test_01_move_message(self):
        text_message = self.dialog.diaologs.item(contains_text='Розница1 Автотестер Продавец').text
        folder = self.folder.folders.row(contains_text='папка для перемещения')

        self.dialog.diaologs.item(contains_text='Розница1 Автотестер Продавец').select_menu_actions("Переместить")
        self.panel.check_load()
        self.panel.move_dialog.row(contains_text='папка для перемещения').click()

        folder.click()
        self.dialog.diaologs.item(item_number=1).should_be(ContainsText(text_message))
        folder.element('[data-qa="msg-folders-counter_total"]').should_be(ExactText('1'))

        self.dialog.diaologs.item(contains_text='Розница1 Автотестер Продавец').select_menu_actions("Переместить")
        self.panel.check_load()
        self.panel.move_dialog.row(contains_text="Все сообщения").element('div').click()
        self.dialog.diaologs.should_be(CountElements(0))
        self.folder.folders.row(contains_text='Все сообщения').click()

    def test_02_check_date(self):
        date_message = self.dialog.diaologs.item(contains_text='Розница1 Автотестер Продавец').element('.msg-entity-date').text
        self.tab.tabs.select("Чаты")
        self.dialog.chats.item(contains_text='Розница1 Автотестер Продавец').element('.msg-entity-date').should_be(ExactText(date_message))
        self.tab.tabs.select(contains_text="Диалоги")

    def test_03_select_tag(self):
        message = self.dialog.diaologs.item(contains_text='Розница1 Автотестер Продавец')
        message.select_menu_actions("Пометить")
        self.panel.control_panel.check_load()
        self.panel.control_panel.item(contains_text='Тест').click()

        self.folder.tags_list.item(contains_text='Тест').element('[data-qa="tag-count-entities"]').should_be(ExactText('1'))
        message.should_be(ContainsText('Тест'))

        message.select_menu_actions("Пометить")
        self.panel.control_panel.check_load()
        self.panel.control_panel.item(contains_text='Тест').click()


