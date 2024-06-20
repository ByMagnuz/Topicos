from PyQt5 import QtCore, QtGui, QtWidgets
from gui.entidad_federativa_gui import EntidadFederativaGUI
from gui.municipio_gui import MunicipioGUI
from gui.destinatario_gui import DestinatarioGUI

class MainMenu(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Menú Principal')
        self.setGeometry(100, 100, 800, 600)  

        # Crear una barra de herramientas
        self.toolBar = QtWidgets.QToolBar(self)
        self.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        # Crear las acciones de la barra de herramientas
        self.entidadesAction = QtWidgets.QAction(QtGui.QIcon('resources/png/16x16/Black pin.png'), 'Entidades Federativas', self)
        self.municipiosAction = QtWidgets.QAction(QtGui.QIcon('resources/png/16x16/Blue pin.png'), 'Municipios', self)
        self.destinatariosAction = QtWidgets.QAction(QtGui.QIcon('resources/png/16x16/Red pin.png'), 'Destinatarios', self)

        # Crear botones con iconos y texto
        self.entidadesButton = QtWidgets.QToolButton()
        self.entidadesButton.setDefaultAction(self.entidadesAction)
        self.entidadesButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        
        self.municipiosButton = QtWidgets.QToolButton()
        self.municipiosButton.setDefaultAction(self.municipiosAction)
        self.municipiosButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        
        self.destinatariosButton = QtWidgets.QToolButton()
        self.destinatariosButton.setDefaultAction(self.destinatariosAction)
        self.destinatariosButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)

        # Añadir botones a la barra de herramientas
        self.toolBar.addWidget(self.entidadesButton)
        self.toolBar.addWidget(self.municipiosButton)
        self.toolBar.addWidget(self.destinatariosButton)

        # Conectar acciones a métodos
        self.entidadesAction.triggered.connect(self.openEntidades)
        self.municipiosAction.triggered.connect(self.openMunicipios)
        self.destinatariosAction.triggered.connect(self.openDestinatarios)

        # Crear el widget central
        self.centralWidget = QtWidgets.QWidget(self)
        self.setCentralWidget(self.centralWidget)
        self.layout = QtWidgets.QVBoxLayout(self.centralWidget)

    def openEntidades(self):
        self.entidadesWindow = EntidadFederativaGUI()
        self.entidadesWindow.show()

    def openMunicipios(self):
        self.municipiosWindow = MunicipioGUI()
        self.municipiosWindow.show()

    def openDestinatarios(self):
        self.destinatariosWindow = DestinatarioGUI()
        self.destinatariosWindow.show()
