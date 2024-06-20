from PyQt5 import QtCore, QtGui, QtWidgets
from control.BDMunicipio import BDMunicipio

ICON_PATH = 'green_circle.png'

class MunicipioGUI(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.bd = BDMunicipio()
        self.setupUi()
        self.loadData()
        self.formVisible = False

    def setupUi(self):
        self.setWindowTitle("Gestión de Municipios")
        self.resize(600, 400)

        self.setStyleSheet("""
            QWidget {
                background-color: #1AA9D3;
            }
            QTableWidget {
                background-color: #87CEEB;
                alternate-background-color: #B0E0E6;
                gridline-color: #d0d0d0;
                width: 100%;
            }
            QHeaderView::section {
                background-color: #0386AC;
                color: #ffffff;
                padding: 4px;
                border: 1px solid #d0d0d0;
                text-transform: uppercase;
            }
            QTableCornerButton::section {
                background-color: #0386AC;
                color: #ffffff;
            }
            QPushButton {
                color: white;
                background-color: #000000;
                border: none;
                padding: 10px;
                text-align: center;
                text-decoration: none;
                display: inline-block;
                font-size: 14px;
                margin: 4px 2px;
                transition-duration: 0.4s;
                cursor: pointer;
            }
            QPushButton#btnNuevo {
                background-color: #808080;
            }
            QPushButton#btnNuevo:hover {
                background-color: #696969;
            }
            QPushButton#btnActualizar {
                background-color: #4CAF50;
            }
            QPushButton#btnActualizar:hover {
                background-color: #45A049;
            }
            QPushButton#btnBorrar {
                background-color: #FF0000;
            }
            QPushButton#btnBorrar:hover {
                background-color: #B22222;
            }
            QPushButton#btnGuardar {
                background-color: #4CAF50;
                color: white;
                border: none;
                padding: 8px 12px;
                font-size: 12px;
                margin-right: 20px;
            }
            QDialogButtonBox QPushButton {
                background-color: #0000FF;
                color: black;
            }
            .green-circle {
                background-image: url('"""+ICON_PATH+"""');
                background-repeat: no-repeat;
                background-position: center;
            }
        """)

        self.layout = QtWidgets.QVBoxLayout(self)

        self.tblDatos = QtWidgets.QTableWidget(self)
        self.tblDatos.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.tblDatos.setAlternatingRowColors(True)
        self.tblDatos.horizontalHeader().setStretchLastSection(True)
        self.tblDatos.verticalHeader().setDefaultSectionSize(24)
        self.layout.addWidget(self.tblDatos)

        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.formNombre = QtWidgets.QLineEdit(self)
        self.formNombre.setObjectName("formNombre")
        self.formIdEntidad = QtWidgets.QLineEdit(self)
        self.formIdEntidad.setObjectName("formIdEntidad")
        self.formLayout.addRow("Nombre:", self.formNombre)
        self.formLayout.addRow("ID Entidad:", self.formIdEntidad)

        self.btnGuardar = QtWidgets.QPushButton("Guardar", self)
        self.btnGuardar.setObjectName("btnGuardar")
        self.formLayout.addRow(self.btnGuardar)

        self.formWidget = QtWidgets.QWidget()
        self.formWidget.setLayout(self.formLayout)
        self.formWidget.hide()

        self.layout.addWidget(self.formWidget)

        self.buttonLayout = QtWidgets.QHBoxLayout()
        self.btnNuevo = QtWidgets.QPushButton("Nuevo", self)
        self.btnNuevo.setObjectName("btnNuevo")
        self.btnActualizar = QtWidgets.QPushButton("Actualizar", self)
        self.btnActualizar.setObjectName("btnActualizar")
        self.btnBorrar = QtWidgets.QPushButton("Borrar", self)
        self.btnBorrar.setObjectName("btnBorrar")

        self.buttonLayout.addWidget(self.btnNuevo)
        self.buttonLayout.addWidget(self.btnActualizar)
        self.buttonLayout.addWidget(self.btnBorrar)
        self.buttonLayout.addStretch()

        self.layout.addLayout(self.buttonLayout)

        self.btnNuevo.clicked.connect(self.toggleForm)
        self.btnActualizar.clicked.connect(self.edit)
        self.btnBorrar.clicked.connect(self.delete)
        self.btnGuardar.clicked.connect(self.save)

    def loadData(self):
        data = self.bd.obtenerDatos()
        if data:
            headers, rows = data
            self.tblDatos.setColumnCount(len(headers))
            self.tblDatos.setRowCount(len(rows))
            headers = [header.upper() for header in headers]
            self.tblDatos.setHorizontalHeaderLabels(headers)
            for row_index, row_data in enumerate(rows):
                for col_index, col_data in enumerate(row_data):
                    item = QtWidgets.QTableWidgetItem(str(col_data))
                    item.setTextAlignment(QtCore.Qt.AlignCenter)
                    if col_data == 1:
                        item.setData(QtCore.Qt.DecorationRole, QtGui.QIcon(ICON_PATH))
                        item.setText("")
                    self.tblDatos.setItem(row_index, col_index, item)

            if "NOMBRE" in headers:
                nombre_index = headers.index("NOMBRE")
                self.tblDatos.horizontalHeader().setSectionResizeMode(nombre_index, QtWidgets.QHeaderView.Stretch)
                for i, header in enumerate(headers):
                    if i != nombre_index:
                        self.tblDatos.horizontalHeader().setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeToContents)

    def toggleForm(self):
        if not self.formVisible:
            self.formWidget.show()
            self.formVisible = True
        else:
            self.formWidget.hide()
            self.formVisible = False

    def edit(self):
        row = self.tblDatos.currentRow()
        if row != -1:
            id_municipio = int(self.tblDatos.item(row, 0).text())
            data = self.bd.obtenerDatosPorID(id_municipio)
            if data:
                self.formNombre.setText(data.get('nombre', ''))
                self.formIdEntidad.setText(str(data.get('id_entidad', '')))
                self.formWidget.show()
                self.formVisible = True

    def save(self):
        nombre = self.formNombre.text()
        id_entidad = self.formIdEntidad.text()
        if nombre and id_entidad.isdigit():
            id_entidad = int(id_entidad)
            mensaje = self.bd.guardar(nombre, id_entidad)
            QtWidgets.QMessageBox.information(self, "Inserción", mensaje)
            self.loadData()
            self.formNombre.clear()
            self.formIdEntidad.clear()
            self.toggleForm()
        else:
            QtWidgets.QMessageBox.critical(self, "Error", "Por favor complete todos los campos correctamente.")

    def delete(self):
        row = self.tblDatos.currentRow()
        if row != -1:
            id = int(self.tblDatos.item(row, 0).text())
            mensaje = self.bd.borrarLogico(id)
            QtWidgets.QMessageBox.information(self, "Borrado", mensaje)
            self.loadData()
        else:
            QtWidgets.QMessageBox.critical(self, "Error", "Seleccione un elemento para borrar.")
