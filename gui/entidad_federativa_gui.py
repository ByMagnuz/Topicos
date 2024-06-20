from PyQt5 import QtCore, QtGui, QtWidgets
from control.BDEntidadFederativa import BDEntidadFederativa

# Ruta al ícono para el círculo verde
ICON_PATH = 'green_circle.png'

class EntidadFederativaGUI(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.bd = BDEntidadFederativa()
        self.setupUi()
        self.loadData()
        self.formVisible = False  # Variable para controlar la visibilidad del formulario de edición

    def setupUi(self):
        self.setWindowTitle("Gestión de Entidades Federativas")
        self.resize(600, 400)

        # Estilo CSS
        self.setStyleSheet("""
            QWidget {
                background-color: #1AA9D3; /* Fondo gris claro */
            }
            QTableWidget {
                background-color: #87CEEB; /* Fondo azul cielo */
                alternate-background-color: #B0E0E6; /* Fondo alternado azul claro */
                gridline-color: #d0d0d0; /* Color de las líneas de la cuadrícula */
                width: 100%; /* Ancho completo */
            }
            QHeaderView::section {
                background-color: #0386AC; /* Fondo negro */
                color: #ffffff; /* Texto blanco */
                padding: 4px;
                border: 1px solid #d0d0d0;
                text-transform: uppercase; /* Texto en mayúsculas */
            }
            QTableCornerButton::section {
                background-color: #0386AC; /* Fondo negro */
                color: #ffffff; /* Texto blanco */
            }
            QTableView QTableCornerButton::section {
                background-color: #000000; /* Fondo negro */
                color: #ffffff; /* Texto blanco */
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
                background-color: #808080; /* Fondo gris */
            }
            QPushButton#btnNuevo:hover {
                background-color: #696969; /* Fondo gris oscuro al pasar el ratón */
            }
            QPushButton#btnActualizar {
                background-color: #4CAF50; /* Fondo verde */
            }
            QPushButton#btnActualizar:hover {
                background-color: #45A049; /* Fondo verde oscuro al pasar el ratón */
            }
            QPushButton#btnBorrar {
                background-color: #FF0000; /* Fondo rojo */
            }
            QPushButton#btnBorrar:hover {
                background-color: #B22222; /* Fondo rojo oscuro al pasar el ratón */
            }
            QPushButton#btnGuardar {
                background-color: #4CAF50; /* Fondo verde */
                color: white; /* Texto blanco */
                border: none;
                padding: 8px 12px; /* Ajustar el padding para que sea más pequeño */
                font-size: 12px; /* Tamaño de fuente menor */
                margin-right: 20px; /* Margen derecho para alinear a la derecha */
            }
            QDialogButtonBox QPushButton {
                background-color: #0000FF; /* Fondo azul */
                color: black; /* Texto negro */
            }
            /* Estilo para mostrar el ícono del círculo verde */
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
        self.formLayout.addRow("Nombre:", self.formNombre)

        self.btnGuardar = QtWidgets.QPushButton("Guardar", self)
        self.btnGuardar.setObjectName("btnGuardar")
        self.formLayout.addRow(self.btnGuardar)

        self.formWidget = QtWidgets.QWidget()
        self.formWidget.setLayout(self.formLayout)
        self.formWidget.hide()  # Ocultar el formulario de edición al inicio

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
        self.buttonLayout.addStretch()  # Añadir espacio flexible a la derecha

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
            self.tblDatos.setRowCount(len(rows))  # Mostrar todas las filas disponibles
            headers = [header.upper() for header in headers]  # Encabezados en mayúsculas
            self.tblDatos.setHorizontalHeaderLabels(headers)
            for row_index, row_data in enumerate(rows):
                for col_index, col_data in enumerate(row_data):
                    item = QtWidgets.QTableWidgetItem(str(col_data))
                    item.setTextAlignment(QtCore.Qt.AlignCenter)  # Centrar texto
                    if col_data == 1:
                        item.setData(QtCore.Qt.DecorationRole, QtGui.QIcon(ICON_PATH))  # Establecer ícono del círculo verde
                        item.setText("")  # Vaciar el texto para mostrar solo el ícono
                    self.tblDatos.setItem(row_index, col_index, item)

            # Ajustar el tamaño de la columna "NOMBRE"
            if "NOMBRE" in headers:
                nombre_index = headers.index("NOMBRE")
                self.tblDatos.horizontalHeader().setSectionResizeMode(nombre_index, QtWidgets.QHeaderView.Stretch)
                for i, header in enumerate(headers):
                    if i != nombre_index:
                        self.tblDatos.horizontalHeader().setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeToContents)

    def toggleForm(self):
        if not self.formVisible:
            self.formWidget.show()  # Mostrar el formulario debajo de la tabla
            self.formVisible = True
        else:
            self.formWidget.hide()  # Ocultar el formulario
            self.formVisible = False

    def edit(self):
        row = self.tblDatos.currentRow()
        if row != -1:
            # Obtener el ID del registro seleccionado (suponiendo que está en la primera columna)
            id = int(self.tblDatos.item(row, 0).text())
            # Obtener los datos del registro para editar
            data = self.bd.obtenerDatosPorID(id)
            if data:
                # Mostrar los datos en el formulario de edición
                nombre = data.get('nombre', '')
                self.formNombre.setText(nombre)
                # Mostrar el formulario de edición
                self.formWidget.show()
                self.formVisible = True

    def save(self):
        nombre = self.formNombre.text()
        if nombre:
            mensaje = self.bd.guardar(nombre)
            QtWidgets.QMessageBox.information(self, "Inserción", mensaje)
            self.loadData()
            self.formNombre.clear()
            self.toggleForm()  # Ocultar el formulario después de guardar

    def delete(self):
        row = self.tblDatos.currentRow()
        if row != -1:
            id = int(self.tblDatos.item(row, 0).text())
            mensaje = self.bd.borrarLogico(id)
            QtWidgets.QMessageBox.information(self, "Borrado", mensaje)
            self.loadData()

