from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget
from PyQt5.uic import loadUi
class VistaInserisciDipendente(QWidget):
    def __init__(self, parent=None):
        super(VistaInserisciDipendente, self).__init__(parent)
        loadUi("NuovoDipendente.ui", self)

    def update_ui(self):
        self.listview_model = QStandardItemModel(self.Lista_Dipendenti)
        for utente in self.controller.get_lista_del_personale():
            item = QStandardItem()
            item.setText(utente.nome + " " + dipendente.cognome)
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            self.listview_model.appendRow(item)
        self.list_view.setModel(self.listview_model)