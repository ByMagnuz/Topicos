from PyQt5 import QtCore, QtGui, QtWidgets
from control.BDEntidadFederativa import BDEntidadFederativa

class EntidadFederativaGUI(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.bd = BDEntidadFederativa()
        self.setupUi()
        self.loadData()

    def setupUi(self):
        self.setWindowTitle("Gestión de Entidades Federativas")
        self.resize(600, 400)
        self.layout = QtWidgets.QVBoxLayout(self)

        self.tblDatos = QtWidgets.QTableWidget(self)
        self.layout.addWidget(self.tblDatos)

        self.btnNuevo = QtWidgets.QPushButton("Nuevo", self)
        self.btnBorrar = QtWidgets.QPushButton("Borrar", self)
        self.layout.addWidget(self.btnNuevo)
        self.layout.addWidget(self.btnBorrar)

        self.btnNuevo.clicked.connect(self.insert)
        self.btnBorrar.clicked.connect(self.delete)

    def loadData(self):
        data = self.bd.obtenerDatos()
        if data:
            headers, rows = data
            self.tblDatos.setColumnCount(len(headers))
            self.tblDatos.setRowCount(len(rows))
            self.tblDatos.setHorizontalHeaderLabels(headers)
            for row_index, row_data in enumerate(rows):
                for col_index, col_data in enumerate(row_data):
                    self.tblDatos.setItem(row_index, col_index, QtWidgets.QTableWidgetItem(str(col_data)))

    def insert(self):
        nombre, ok = QtWidgets.QInputDialog.getText(self, 'Nueva Entidad Federativa', 'Nombre:')
        if ok and nombre:
            mensaje = self.bd.guardar(nombre)
            QtWidgets.QMessageBox.information(self, "Inserción", mensaje)
            self.loadData()

    def delete(self):
        row = self.tblDatos.currentRow()
        if row != -1:
            id = int(self.tblDatos.item(row, 0).text())
            mensaje = self.bd.borrarLogico(id)
            QtWidgets.QMessageBox.information(self, "Borrado", mensaje)
            self.loadData()
