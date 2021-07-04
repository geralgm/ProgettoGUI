import sys  # Modulo che fornisce l'accesso ad alcune variabili , in questo caso sys.exit
from PyQt5.QtWidgets import QApplication, QWidget
from home.views.GUI_Home import GUI_Home  # importa dalla directory home "VistaHome"

if __name__ == '__main__':
    app = QApplication(sys.argv)
    vista_home = GUI_Home()
    vista_home.show()
    sys.exit(app.exec())
