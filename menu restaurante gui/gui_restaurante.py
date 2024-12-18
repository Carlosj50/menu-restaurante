import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QPushButton,
    QListWidget, QMessageBox
)
from PyQt6.QtGui import QPainter, QFont
from PyQt6.QtPrintSupport import QPrinter, QPrintDialog
from menus import *


class RestauranteGUI(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Sistema de Comandas")
        self.setGeometry(100, 100, 400, 300)

        # Diccionario de menús
        self.menus_dict = {
            "Pastas": menu_pastas,
            "Carnes": menu_carnes,
            "Pescados y Mariscos": menu_pescados,
            "Vegetariano": menu_vegetariano,
            "Postres": menu_postres,
            "Bebidas": menu_bebidas,
        }

        # Comanda (lista de platos seleccionados)
        self.comanda = []

        # Layout principal
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # Etiqueta del título
        self.title_label = QLabel("Selecciona un tipo de plato:")
        self.layout.addWidget(self.title_label)

        # Lista de nombres de menús
        self.menu_list = QListWidget()
        self.menu_list.addItems(self.menus_dict.keys())
        self.layout.addWidget(self.menu_list)

        # Botón para seleccionar el menú
        self.select_menu_button = QPushButton("Seleccionar Menú")
        self.select_menu_button.clicked.connect(self.mostrar_menu_platos)
        self.layout.addWidget(self.select_menu_button)

        # Botón para ver la comanda
        self.view_comanda_button = QPushButton("Ver Comanda")
        self.view_comanda_button.clicked.connect(self.mostrar_comanda)
        self.layout.addWidget(self.view_comanda_button)

        # Botón para imprimir la comanda
        self.print_comanda_button = QPushButton("Imprimir Comanda")
        self.print_comanda_button.clicked.connect(self.imprimir_comanda)
        self.layout.addWidget(self.print_comanda_button)

        # Botón para salir del programa
        self.exit_button = QPushButton("Salir del Programa")
        self.exit_button.clicked.connect(self.salir_del_programa)
        self.layout.addWidget(self.exit_button)

    def mostrar_menu_platos(self):
        selected_menu = self.menu_list.currentItem()
        if selected_menu:
            menu_name = selected_menu.text()
            platos = self.menus_dict[menu_name]

            self.platos_window = QWidget()
            self.platos_window.setWindowTitle(f"Menú de {menu_name}")
            self.platos_window.setGeometry(150, 150, 400, 300)
            layout = QVBoxLayout()

            layout.addWidget(QLabel(f"Menú de {menu_name}:"))

            self.plato_list = QListWidget()
            self.plato_list.addItems(platos)
            layout.addWidget(self.plato_list)

            add_button = QPushButton("Añadir Plato")
            add_button.clicked.connect(lambda: self.agregar_plato(menu_name))
            layout.addWidget(add_button)

            back_button = QPushButton("Volver al Menú Principal")
            back_button.clicked.connect(self.platos_window.close)
            layout.addWidget(back_button)

            self.platos_window.setLayout(layout)
            self.platos_window.show()
        else:
            QMessageBox.warning(self, "Error", "Por favor, selecciona un tipo de plato.")

    def agregar_plato(self, menu_name):
        selected_plato = self.plato_list.currentItem()
        if selected_plato:
            plato = selected_plato.text()
            self.comanda.append(f"{plato} (Menú de {menu_name})")
            QMessageBox.information(self, "Plato Añadido", f"Has añadido: {plato}")
        else:
            QMessageBox.warning(self, "Error", "Por favor, selecciona un plato para añadir.")

    def mostrar_comanda(self):
        if self.comanda:
            comanda_text = "\n".join(self.comanda)
            QMessageBox.information(self, "Comanda", f"Resumen del pedido:\n{comanda_text}")
        else:
            QMessageBox.information(self, "Comanda Vacía", "No has seleccionado ningún plato.")

    def imprimir_comanda(self):
        if not self.comanda:
            QMessageBox.warning(self, "Comanda Vacía", "No hay platos en la comanda para imprimir.")
            return

        printer = QPrinter()
        dialog = QPrintDialog(printer, self)

        if dialog.exec():
            painter = QPainter(printer)
            painter.setFont(QFont("Arial", 12))
            y_position = 100

            painter.drawText(100, y_position, "Comanda del Restaurante")
            y_position += 50

            for plato in self.comanda:
                painter.drawText(100, y_position, plato)
                y_position += 30

            painter.end()
            QMessageBox.information(self, "Impresión Exitosa", "La comanda se ha enviado a la impresora.")

    def salir_del_programa(self):
        respuesta = QMessageBox.question(
            self, "Salir", "¿Estás seguro de que quieres salir del programa?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        if respuesta == QMessageBox.StandardButton.Yes:
            sys.exit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RestauranteGUI()
    window.show()
    sys.exit(app.exec())
