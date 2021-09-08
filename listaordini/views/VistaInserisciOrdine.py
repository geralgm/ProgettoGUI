from PyQt5.QtWidgets import QLineEdit, QLabel, QMessageBox, QPushButton, QSpacerItem, QSizePolicy, QVBoxLayout, QWidget

from ordine.model.Ordine import Ordine


class VistaInserisciOrdine(QWidget):
    def __init__(self, controller, callback):
        super(VistaInserisciOrdine, self).__init__()
        self.controller = controller
        self.callback = callback
        self.info = {}

        self.v_layout = QVBoxLayout()
        self.qlines = {}
        self.add_info_text("cod_fattura", "Codice fattura")
        self.add_info_text("stato", "Stato")
        self.add_info_text("numero_tavola", "Numero tavola")
        self.add_info_text("data_ordine", "Data dell'ordine (dd/mm/AAAA)")
        self.add_info_text("importo_totale", "importo totale")
        self.add_info_text("quantita_totale", "Quantita totale")

        self.v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_ok = QPushButton("OK")
        btn_ok.clicked.connect(self.inserisci_ordine)
        self.v_layout.addWidget(btn_ok)

        self.setLayout(self.v_layout)
        self.setWindowTitle("New")

    def add_info_text(self, nome, label):
        self.v_layout.addWidget(QLabel(label))
        current_text = QLineEdit(self)
        self.qlines[nome] = current_text
        self.v_layout.addWidget(current_text)




    def inserisci_ordine(self):
        for value in self.qlines.values():
            if value.text() == "":
                QMessageBox.critical(self, 'Errore', 'Per favore, inserisci tutte le informazioni richieste.', QMessageBox.Ok, QMessageBox.Ok)
                return

        #cod_fattura = self.info["cod_fattura"].text()
        #stato = self.info["stato"].text()
        #numero_tavola = self.info["numero_tavola"].text()
        #data_ordine = self.info["data_ordine"].text()
        #importo_totale = self.info["importo_totale"].text()
        #quantita_totale = self.info["quantita_totale"].text()
        self.controller.aggiungi_ordine(Ordine(
            (self.qlines["cod_fattura"].text()).lower(),
            #self.qlines["cod_fattura"].text(),
            self.qlines["stato"].text(),
            self.qlines["numero_tavola"].text(),
            self.qlines["data_ordine"].text(),
            self.qlines["importo_totale"].text(),
            self.qlines["quantita_totale"].text())
        )




       # for value in self.info.values():
            #if value.text() == "":
              # QMessageBox.critical(self, 'Inserisci tutte le informazioni richieste', QMessageBox.Ok, QMessageBox.Ok)
               #return

        #self.controller.aggiungi_ordine(Ordine(cod_fattura, stato, numero_tavola
        #                                      , data_ordine,importo_totale, quantita_totale))

        self.callback()
        self.close()