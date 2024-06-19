from PyQt5 import QtCore, QtGui, QtWidgets
from control.BDDestinatario import BDDestinatario

class DestinatarioGUI(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Gestión de Destinatarios')
        self.setGeometry(100, 100, 800, 600)

        self.layout = QtWidgets.QVBoxLayout(self)

        self.table = QtWidgets.QTableWidget(self)
        self.table.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
        self.table.setSelectionMode(QtWidgets.QTableView.SingleSelection)
        self.table.itemSelectionChanged.connect(self.fillForm)
        self.layout.addWidget(self.table)

        self.formLayout = QtWidgets.QFormLayout()
        self.layout.addLayout(self.formLayout)

        self.nombreInput = QtWidgets.QLineEdit(self)
        self.formLayout.addRow('Nombre del Destinatario:', self.nombreInput)

        self.direccionInput = QtWidgets.QLineEdit(self)
        self.formLayout.addRow('Dirección:', self.direccionInput)

        self.idMunicipioInput = QtWidgets.QLineEdit(self)
        self.formLayout.addRow('ID del Municipio:', self.idMunicipioInput)

        self.buttonLayout = QtWidgets.QHBoxLayout()
        self.layout.addLayout(self.buttonLayout)

        self.addButton = QtWidgets.QPushButton('Agregar', self)
        self.addButton.clicked.connect(self.addDestinatario)
        self.buttonLayout.addWidget(self.addButton)

        self.updateButton = QtWidgets.QPushButton('Actualizar', self)
        self.updateButton.clicked.connect(self.updateDestinatario)
        self.buttonLayout.addWidget(self.updateButton)

        self.deleteButton = QtWidgets.QPushButton('Eliminar', self)
        self.deleteButton.clicked.connect(self.deleteDestinatario)
        self.buttonLayout.addWidget(self.deleteButton)

        self.loadData()

    def loadData(self):
        self.table.clear()
        db = BDDestinatario()
        data, error = db.obtenerDatos()
        if error:
            QtWidgets.QMessageBox.critical(self, "Error en la base de datos", error)
            return
        columns, data = data
        self.table.setColumnCount(len(columns))
        self.table.setRowCount(len(data))
        self.table.setHorizontalHeaderLabels(columns)
        for row_num, row_data in enumerate(data):
            for col_num, col_data in enumerate(row_data):
                self.table.setItem(row_num, col_num, QtWidgets.QTableWidgetItem(str(col_data)))
        self.table.resizeColumnsToContents()

    def fillForm(self):
        selected_row = self.table.currentRow()
        if selected_row != -1:
            self.nombreInput.setText(self.table.item(selected_row, 1).text())
            self.direccionInput.setText(self.table.item(selected_row, 2).text())
            self.idMunicipioInput.setText(self.table.item(selected_row, 3).text())

    def addDestinatario(self):
        nombre = self.nombreInput.text()
        direccion = self.direccionInput.text()
        id_municipio = self.idMunicipioInput.text()
        if not nombre or not direccion or not id_municipio:
            QtWidgets.QMessageBox.warning(self, "Advertencia", "Todos los campos deben estar llenos")
            return
        db = BDDestinatario()
        success, error = db.guardar(nombre, direccion, id_municipio)
        if error:
            QtWidgets.QMessageBox.critical(self, "Error en la base de datos", error)
        else:
            self.loadData()
            self.nombreInput.clear()
            self.direccionInput.clear()
            self.idMunicipioInput.clear()

    def updateDestinatario(self):
        selected_row = self.table.currentRow()
        if selected_row != -1:
            id = int(self.table.item(selected_row, 0).text())
            nombre = self.nombreInput.text()
            direccion = self.direccionInput.text()
            id_municipio = self.idMunicipioInput.text()
            if not nombre or not direccion or not id_municipio:
                QtWidgets.QMessageBox.warning(self, "Advertencia", "Todos los campos deben estar llenos")
                return
            db = BDDestinatario()
            success, error = db.actualizar(id, nombre, direccion, id_municipio)
            if error:
                QtWidgets.QMessageBox.critical(self, "Error en la base de datos", error)
            else:
                self.loadData()
                self.nombreInput.clear()
                self.direccionInput.clear()
                self.idMunicipioInput.clear()

    def deleteDestinatario(self):
        selected_row = self.table.currentRow()
        if selected_row != -1:
            id = int(self.table.item(selected_row, 0).text())
            db = BDDestinatario()
            success, error = db.borrar(id)
            if error:
                QtWidgets.QMessageBox.critical(self, "Error en la base de datos", error)
            else:
                self.loadData()
