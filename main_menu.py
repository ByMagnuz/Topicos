from PyQt5 import QtWidgets
from gui.entidad_federativa_gui import EntidadFederativaGUI
from gui.municipio_gui import MunicipioGUI
from gui.destinatario_gui import DestinatarioGUI

class MainMenu(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Menú Principal')
        self.setGeometry(100, 100, 400, 300)

        self.centralWidget = QtWidgets.QWidget()
        self.setCentralWidget(self.centralWidget)

        self.layout = QtWidgets.QVBoxLayout(self.centralWidget)

        self.entidadesButton = QtWidgets.QPushButton('Gestión de Entidades Federativas', self)
        self.entidadesButton.clicked.connect(self.openEntidades)
        self.layout.addWidget(self.entidadesButton)

        self.municipiosButton = QtWidgets.QPushButton('Gestión de Municipios', self)
        self.municipiosButton.clicked.connect(self.openMunicipios)
        self.layout.addWidget(self.municipiosButton)

        self.destinatariosButton = QtWidgets.QPushButton('Gestión de Destinatarios', self)
        self.destinatariosButton.clicked.connect(self.openDestinatarios)
        self.layout.addWidget(self.destinatariosButton)

    def openEntidades(self):
        self.entidadesWindow = EntidadFederativaGUI()
        self.entidadesWindow.show()

    def openMunicipios(self):
        self.municipiosWindow = MunicipioGUI()
        self.municipiosWindow.show()

    def openDestinatarios(self):
        self.destinatariosWindow = DestinatarioGUI()
        self.destinatariosWindow.show()
