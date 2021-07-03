import sys  # Modulo che fornisce l'accesso ad alcune variabili , in questo caso sys.exit

from PyQt5.QtGui import QStandardItem
from PyQt5.QtWidgets import QWidget
# from PyQt5 import uic
from PyQt5.uic import loadUi
from listadipendenti.views.VistaInserisciDipendente import VistaInserisciDipendente

class VistaListaDipendenti(QWidget):
    def __init__(self, parent=None):
        super(VistaListaDipendenti, self).__init__(parent)
        loadUi("GUI_ListaDipendenti.ui", self)
        self.Button_NuovoDipendente.clicked.connect(self.go_nuovo_dipendente)
    def go_nuovo_dipendente(self):
        vista_nuovo_dipendente = VistaInserisciDipendente(self)
        vista_nuovo_dipendente.show()


    #def go_apri_dipendente(selfself):
     #   vista_dipendente = VistaDipendente(self)
      #  vista_dipendente.show()


    #da modificare




    def closeEvent(self, event):
        self.controller.save_data()

    #def show_dipendente(self):
        #if (len(self.list_view.selectedIndexes()) > 0):
            #selected = self.list_view.selectedIndexes()[0].row()
            #dipendente_selezionato = self.controller.get_dipendente_by_index(selected)
            #self.vista_dipendente = VistaDipendente(dipendente_selezionato, self.controller.elimina_dipendente_by_codice, self.update_ui)
           # self.vista_utente.show()
