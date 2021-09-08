from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QSpacerItem, QSizePolicy, QPushButton

from cliente.controller.ControlloreCliente import ControlloreCliente


class VistaCliente(QWidget):
    def __init__(self, cliente, elimina_cliente, elimina_callback, parent=None):
        super(VistaCliente, self).__init__(parent)
        self.controller = ControlloreCliente(cliente)
        self.elimina_cliente = elimina_cliente
        self.elimina_callback = elimina_callback

        v_layout = QVBoxLayout()

        label_nome = QLabel(self.controller.get_nome_cliente() + " " + self.controller.get_cognome_cliente())
        font_nome = label_nome.font()
        font_nome.setPointSize(30)
        label_nome.setFont(font_nome)
        v_layout.addWidget(label_nome)

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        v_layout.addWidget(self.get_info("Codice Fiscale: {}".format(self.controller.get_cf_cliente())))
        v_layout.addWidget(self.get_info("Data Nascita: {}".format(self.controller.get_datanascita_cliente())))
        v_layout.addWidget(self.get_info("Email: {}".format(self.controller.get_email_cliente())))
        v_layout.addWidget(self.get_info("Telefono: {}".format(self.controller.get_telefono_cliente())))
        v_layout.addWidget(self.get_info("Indirizzo: {}".format(self.controller.get_indirizzo_cliente())))




        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_elimina = QPushButton("Elimina")
        btn_elimina.clicked.connect(self.elimina_cliente_click)
        v_layout.addWidget(btn_elimina)

        self.setLayout(v_layout)
        self.setWindowTitle(self.controller.get_nome_cliente())

    def get_info(self, text):
        label = QLabel(text)
        font = label.font()
        font.setPointSize(17)
        label.setFont(font)
        return label

    def elimina_cliente_click(self):
        self.elimina_cliente(self.controller.get_id_cliente())
        self.elimina_callback()
        self.close()