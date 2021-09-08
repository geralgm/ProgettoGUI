from PyQt5.QtCore import QSize, QRect
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QPixmap
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QListView, QLabel
from PyQt5 import QtCore, QtGui, QtWidgets

from cliente.views.VistaCliente import VistaCliente
from listaclienti.controller.ControlloreListaClienti import ControlloreListaClienti
from listaclienti.views.VistaInserisciCliente import VistaInserisciCliente
import images, images2

class VistaListaClienti(QWidget):
    def __init__(self, parent=None):
        super(VistaListaClienti, self).__init__(parent)

        self.controller = ControlloreListaClienti()

        self.setObjectName("VistaClienti")
        self.resize(730, 600)
        self.setMinimumSize(QSize(730, 600))
        self.setMaximumSize(QSize(730, 600))


        self.sfondo = QLabel(self)
        self.sfondo.setObjectName(u"sfondo")
        self.sfondo.setGeometry(QRect(0, 0, 730, 600))
        self.sfondo.setPixmap(QPixmap(u":/newPrefix/textureCliente.jpg"))
        self.sfondo.setScaledContents(True)

        h_layout = QHBoxLayout()
        self.list_view = QListView(self)
        self.list_view.setGeometry(QRect(20, 80, 500, 450))
        self.list_view.setObjectName("listWidget")
        self.update_ui()
        h_layout.addWidget(self.list_view)



        #buttons_layout = QVBoxLayout()
        #open_button = QPushButton('Apri')
        #open_button.clicked.connect(self.show_selected_info)
        #buttons_layout.addWidget(open_button)
        #new_button = QPushButton("Nuovo")
        #new_button.clicked.connect(self.show_new_dipendente)
        #buttons_layout.addWidget(new_button)
        #buttons_layout.addStretch()
        #h_layout.addLayout(buttons_layout)
        self.Button_ApriCliente = QtWidgets.QPushButton(self)
        self.Button_ApriCliente.setGeometry(QtCore.QRect(550, 80, 150, 70))
        self.Button_ApriCliente.setStyleSheet("QPushButton#Button_ApriCliente{\n"
                                                 "  background-color:#293d3d;\n"
                                                 "  border-radius: 30px;\n"
                                                 "  color: white;\n"
                                                 "  padding: 16px 32px;\n"
                                                 "  text-align: center;\n"
                                                 "  text-decoration: none;\n"
                                                 "  display: inline-block;\n"
                                                 "  font-size: 16px;\n"
                                                 "  margin: 4px 2px;\n"
                                                 "  transition-duration: 0.4s;\n"
                                                 "  cursor: pointer;\n"
                                                 "}\n"
                                                 "QPushButton#Button_ApriCliente:pressed{\n"
                                                 " background-color: white; \n"
                                                 "  color: black; \n"
                                                 "  border: 3px solid #4CAF50;\n"
                                                 "}\n"
                                                 "QPushButton#Button_ApriCliente:hover {background-color:      #d1e0e0;}\n"
                                                 "")
        self.Button_ApriCliente.setObjectName("Button_ApriCliente")


        self.Button_NuovoCliente = QtWidgets.QPushButton(self)
        self.Button_NuovoCliente.setGeometry(QtCore.QRect(550, 160, 150, 70))
        self.Button_NuovoCliente.setStyleSheet("QPushButton#Button_NuovoCliente{\n"
                                                  "  background-color:#293d3d;\n"
                                                  "  border-radius: 30px;\n"
                                                  "  color: white;\n"
                                                  "  padding: 16px 32px;\n"
                                                  "  text-align: center;\n"
                                                  "  text-decoration: none;\n"
                                                  "  display: inline-block;\n"
                                                  "  font-size: 16px;\n"
                                                  "  margin: 4px 2px;\n"
                                                  "  transition-duration: 0.4s;\n"
                                                  "  cursor: pointer;\n"
                                                  "}\n"
                                                  "QPushButton#Button_NuovoCliente:pressed{\n"
                                                  " background-color: white; \n"
                                                  "  color: black; \n"
                                                  "  border: 3px solid #4CAF50;\n"
                                                  "}\n"
                                                  "QPushButton#Button_NuovoCliente:hover {background-color:      #d1e0e0;}")
        self.Button_NuovoCliente.setObjectName("Button_NuovoCliente")

        self.Button_Home = QtWidgets.QPushButton(self)
        self.Button_Home.setGeometry(QtCore.QRect(550, 240, 150, 70))
        #font = QtGui.QFont()
        #font.setFamily("HoloLens MDL2 Assets")
        #font.setPointSize(-1)
        #font.setUnderline(False)
        #font.setStrikeOut(False)
       # self.Button_Home.setFont(font)
        self.Button_Home.setStyleSheet("QPushButton#Button_Home{\n"
                                       "  background-color:#293d3d;\n"
                                       "  border-radius: 30px;\n"
                                       "  color: white;\n"
                                       "  padding: 16px 32px;\n"
                                       "  text-align: center;\n"
                                       "  text-decoration: none;\n"
                                       "  display: inline-block;\n"
                                       "  font-size: 20px;\n"
                                       "  margin: 4px 2px;\n"
                                       "  transition-duration: 0.4s;\n"
                                       "  cursor: pointer;\n"
                                       "}\n"
                                       "QPushButton#Button_Home:pressed{\n"
                                       " background-color: white; \n"
                                       "  color: black; \n"
                                       "  border: 3px solid #4CAF50;\n"
                                       "}\n"
                                       "QPushButton#Button_Home:hover {background-color:      #d1e0e0;}\n"
                                       "")
        self.Button_Home.setObjectName("Button_Home")

        self.Button_ApriCliente.clicked.connect(self.show_selected_info)
        self.Button_NuovoCliente.clicked.connect(self.show_new_cliente)
        self.Button_Home.clicked.connect(self.close)

      #  self.setLayout(h_layout)
     #   self.resize(500,200)
      #  self.setWindowTitle('Lista Dipendenti')

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def update_ui(self):
        self.listview_model = QStandardItemModel(self.list_view)
        for cliente in self.controller.get_lista_clienti():
            item = QStandardItem()
            item.setText(cliente.nome + " " + cliente.cognome)
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            self.listview_model.appendRow(item)
        self.list_view.setModel(self.listview_model)

    def show_selected_info(self):
        if(len(self.list_view.selectedIndexes()) > 0):
            selected = self.list_view.selectedIndexes()[0].row()
            cliente_selezionato = self.controller.get_cliente_by_index(selected)
            self.vista_cliente = VistaCliente(cliente_selezionato, self.controller.elimina_cliente_by_id, self.update_ui)
            self.vista_cliente.show()

    def show_new_cliente(self):
        self.vista_inserisci_cliente = VistaInserisciCliente(self.controller, self.update_ui)
        self.vista_inserisci_cliente.show()

    def closeEvent(self, event):
        self.controller.save_data()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("VistaListaClienti", "Form"))
        self.Button_ApriCliente.setText(_translate("VistaListaClienti", "Apri"))
        self.Button_NuovoCliente.setText(_translate("VistaListaClienti", "Nuovo"))
        self.Button_Home.setText(_translate("VistaListaClienti", ""))