from PyQt5 import QtCore, QtGui, QtWidgets
from control.BDMunicipio import BDMunicipio

class MunicipioGUI(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Gestión de Municipios')
        self.setGeometry(100, 100, 600, 400)

        self.layout = QtWidgets.QVBoxLayout(self)

        self.table = QtWidgets.QTableWidget(self)
        self.layout.addWidget(self.table)

        self.formLayout = QtWidgets.QFormLayout()
        self.layout.addLayout(self.formLayout)

        self.nombreInput = QtWidgets.QLineEdit(self)
        self.formLayout.addRow('Nombre del Municipio:', self.nombreInput)

        self.idEntidadInput = QtWidgets.QLineEdit(self)
        self.formLayout.addRow('ID de la Entidad Federativa:', self.idEntidadInput)

        self.buttonLayout = QtWidgets.QHBoxLayout()
        self.layout.addLayout(self.buttonLayout)

        self.addButton = QtWidgets.QPushButton('Agregar', self)
        self.addButton.clicked.connect(self.addMunicipio)
        self.buttonLayout.addWidget(self.addButton)

        self.updateButton = QtWidgets.QPushButton('Actualizar', self)
        self.updateButton.clicked.connect(self.updateMunicipio)
        self.buttonLayout.addWidget(self.updateButton)

        self.deleteButton = QtWidgets.QPushButton('Eliminar', self)
        self.deleteButton.clicked.connect(self.deleteMunicipio)
        self.buttonLayout.addWidget(self.deleteButton)

        self.loadData()

    def loadData(self):
        self.table.clear()
        db = BDMunicipio()
        data, error = db.obtenerDatos()
        if error:
            QtWidgets.QMessageBox.critical(self, "Error en la base de datos", error)
            return
        columns, data = data
        self.table.setColumnCount(len(columns))
        self.table.setHorizontalHeaderLabels(columns)
        self.table.setRowCount(len(data))
        for row_num, row_data in enumerate(data):
            for col_num, col_data in enumerate(row_data):
                self.table.setItem(row_num, col_num, QtWidgets.QTableWidgetItem(str(col_data)))

    def addMunicipio(self):
        nombre = self.nombreInput.text()
        id_entidad = self.idEntidadInput.text()
        if not nombre or not id_entidad:
            QtWidgets.QMessageBox.warning(self, "Advertencia", "Todos los campos deben estar llenos")
            return
        db = BDMunicipio()
        success, error = db.guardar(nombre, id_entidad)
        if error:
            QtWidgets.QMessageBox.critical(self, "Error en la base de datos", error)
        else:
            self.loadData()
            self.nombreInput.clear()
            self.idEntidadInput.clear()

    def updateMunicipio(self):
        selected_row = self.table.currentRow()
        if selected_row != -1:
            id = int(self.table.item(selected_row, 0).text())
            nombre = self.nombreInput.text()
            id_entidad = self.idEntidadInput.text()
            if not nombre or not id_entidad:
                QtWidgets.QMessageBox.warning(self, "Advertencia", "Todos los campos deben estar llenos")
                return
            db = BDMunicipio()
            success, error = db.actualizar(id, nombre, id_entidad)
            if error:
                QtWidgets.QMessageBox.critical(self, "Error en la base de datos", error)
            else:
                self.loadData()
                self.nombreInput.clear()
                self.idEntidadInput.clear()

    def deleteMunicipio(self):
        selected_row = self.table.currentRow()
        if selected_row != -1:
            id = int(self.table.item(selected_row, 0).text())
            db = BDMunicipio()
            success, error = db.borrar(id)
            if error:
                QtWidgets.QMessageBox.critical(self, "Error en la base de datos", error)
            else:
                self.loadData()
