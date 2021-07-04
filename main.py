import sys  # Modulo che fornisce l'accesso ad alcune variabili , in questo caso sys.exit
from PyQt5.QtWidgets import QApplication, QWidget
from home.views.GUI_Home import Ui_Home  # importa dalla directory home "VistaHome"

class MyQWidget(QWidget, Ui_Home):
    def __init__(self, parent=None):
        super(MyQWidget, self).__init__(parent)
        self.setupUi(self)
if __name__ == '__main__':

    app = QApplication(sys.argv)
    main = MyQWidget()
    main.show()
    app.exec_()
