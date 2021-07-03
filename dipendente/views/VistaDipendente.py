from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QSpacerItem, QSizePolicy, QPushButton
from PyQt5.uic import loadUi

from dipendente.controller.ControlloreDipendente import ControlloreDipendente


class VistaDipendente(QWidget):
    def __init__(self, dipendente, elimina_dipendente, elimina_callback, parent=None):
        super(VistaDipendente, self).__init__(parent)
        self.controller = ControlloreDipendente(dipendente)
        self.elimina_dipendente = elimina_dipendente
        self.elimina_callback = elimina_callback

        loadUi("GUI_ListaDipendenti.ui", self)

        label_nome = self.controller.get_nome_dipendente() + " " + self.controller.get_cognome_dipendente()
        font_nome = label_nome.font()
        font_nome.setPointSize(30)
        label_nome.setFont(font_nome)



        self.get_info("Codice Fiscale: {}".format(self.controller.get_cf_dipendente()))
        self.get_info("Data Nascita: {}".format(self.controller.get_datanascita_dipendente()))
        self.get_info("Email: {}".format(self.controller.get_email_dipendente()))
        self.get_info("Telefono: {}".format(self.controller.get_telefono_dipendente()))
        self.get_info("Residenza: {}".format(self.controller.get_residenza_dipendente()))
        self.get_info("CAP: {}".format(self.controller.get_cap_dipendente()))
        self.get_info("Professione: {}".format(self.controller.get_professione_dipendente()))


        self.Button_Elimina.clicked.connect(self.elimina_dipendente_click)



        self.setWindowTitle(self.controller.get_nome_dipendente())

    def get_info(self, text):
        label = QLabel(text)
        font = label.font()
        font.setPointSize(17)
        label.setFont(font)
        return label

    def elimina_dipendente_click(self):
        self.elimina_dipendente(self.controller.get_id_dipendente())
        self.elimina_callback()
        self.close()