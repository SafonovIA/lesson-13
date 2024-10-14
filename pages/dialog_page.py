from atf.ui import *
from controls import *


class Dialog(Region):
    diaologs = ControlsListView(By.CSS_SELECTOR, '.msg-dialogs-detail__list .controls-ListViewV__itemsContainer', 'Диалоги')
    chats = ControlsListView(By.CSS_SELECTOR, '.msg-CorrespondenceDetail .controls-ListViewV__itemsContainer', 'Чаты')

    def check_load(self):
        self.diaologs.check_load()


class Folders(Region):
    folders = ControlsTreeGridView(By.CSS_SELECTOR, '.controls-MasterDetail_master-template .controls-Grid', 'Папки')
    tags_list = ControlsListView(By.CSS_SELECTOR, '.tags-list', 'Теги')


    def check_load(self):
        self.folders.check_load()


class Panel(Region):
    move_dialog = ControlsTreeGridView(By.CSS_SELECTOR, '.controls-Popup .controls-Grid', "Список для перемещения")
    control_panel = ControlsListView(By.CSS_SELECTOR, '.controls-Popup .controls-ListViewV', "Список для тегов")

    def check_load(self):
        self.move_dialog.check_load()


class Tabs(Region):
    tabs = ControlsTabsButtons()