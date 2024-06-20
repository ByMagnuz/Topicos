from PyQt5 import QtWidgets
from main_menu import MainMenu
import sys

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainMenu()
    window.show()
    sys.exit(app.exec_())
