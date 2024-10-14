from atf.ui import *
from controls import *


class MainPage(Region):
    diaologs = ControlsListView(By.CSS_SELECTOR, '.msg-dialogs-detail__list .controls-ListViewV__itemsContainer', 'Диалоги')
    tabs = ControlsTabsButtons()
    folders = ControlsTreeGridView(By.CSS_SELECTOR, '.controls-MasterDetail_master-template .controls-Grid', 'Папки')
    tags_list = ControlsListView(By.CSS_SELECTOR, '.tags-list', 'Теги')

    count_folder = folders.row(contains_text='папка для перемещения').should_be(Displayed).element('[data-qa="msg-folders-counter_total"]')
    date_message = diaologs.item(contains_text='Сообщение').should_be(Displayed).element('.msg-entity-date')
    count_tag = tags_list.item(contains_text='Тест').should_be(Displayed).element('[data-qa="tag-count-entities"]')
    marker_folders = folders.row(contains_text='папка для перемещения').element('[data-qa="marker"]')
    marker_tabs = tabs.item(contains_text='Чаты').element('.controls-Tabs__marker')

    def check_load(self):
        self.diaologs.check_load()


class Chats(Region):
    chats = ControlsListView(By.CSS_SELECTOR, '.msg-CorrespondenceDetail .controls-ListViewV__itemsContainer', 'Чаты')

    date_message = chats.item(contains_text='Сообщение').element('.msg-entity-date')

    def check_load(self):
        self.chats.check_load()


class PanelMoveDialog(Region):
    move_dialog = ControlsTreeGridView(By.CSS_SELECTOR, '.controls-Popup .controls-Grid', "Список для перемещения")

    def check_load(self):
        self.move_dialog.check_load()


class ControlPanel(Region):
    panel = ControlsListView(By.CSS_SELECTOR, '.controls-Popup .controls-ListViewV', "Список для тегов")

    def check_load(self):
        self.panel.check_load()

