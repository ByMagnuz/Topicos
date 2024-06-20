from PyQt5 import QtWidgets
from main_menu import MainMenu
import sys

def main():
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainMenu()
    mainWindow.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
