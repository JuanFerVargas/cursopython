import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QLabel, QDialog

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Ventana de Login
        self.setWindowTitle("Login")
        self.setGeometry(300, 300, 300, 150)

        # Elementos de la interfaz
        self.username_label = QLabel("Usuario:")
        self.password_label = QLabel("Contraseña:")
        self.username_input = QLineEdit()
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        self.login_button = QPushButton("Ingresar")
        self.exit_button = QPushButton("Salir")

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_button)
        layout.addWidget(self.exit_button)

        # Conectar botones
        self.login_button.clicked.connect(self.check_login)
        self.exit_button.clicked.connect(self.close)

        self.setLayout(layout)

    def check_login(self):
        # Comprobación simple de login (usuario y contraseña predeterminados)
        user = self.username_input.text()
        password = self.password_input.text()

        if user == "admin" and password == "1234":
            self.accept_login()
        else:
            self.show_error("Usuario o contraseña incorrectos.")

    def accept_login(self):
        # Cerrar la ventana de login y abrir la ventana principal
        self.hide()
        self.main_window = MainWindow()
        self.main_window.show()

    def show_error(self, message):
        # Función para mostrar error en caso de login incorrecto
        error_dialog = QDialog(self)
        error_dialog.setWindowTitle("Error")
        error_layout = QVBoxLayout()
        error_layout.addWidget(QLabel(message))
        error_dialog.setLayout(error_layout)
        error_dialog.exec_()

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Ventana principal
        self.setWindowTitle("Bienvenido")
        self.setGeometry(300, 300, 300, 200)

        # Elementos de la interfaz
        self.welcome_label = QLabel("¡Bienvenido al sistema!")
        self.cancel_button = QPushButton("Cancelar")
        self.suspend_button = QPushButton("Suspender y Levantar")
        self.exit_button = QPushButton("Salir")

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.welcome_label)
        layout.addWidget(self.cancel_button)
        layout.addWidget(self.suspend_button)
        layout.addWidget(self.exit_button)

        # Conectar botones
        self.cancel_button.clicked.connect(self.cancel_action)
        self.suspend_button.clicked.connect(self.suspend_action)
        self.exit_button.clicked.connect(self.exit_action)

        self.setLayout(layout)

    def cancel_action(self):
        # Acción para el botón Cancelar
        self.close()

    def suspend_action(self):
        # Acción para el botón Suspender y Levantar
        self.suspend_button.setText("Levantar")
        self.suspend_button.clicked.disconnect()
        self.suspend_button.clicked.connect(self.raise_action)

    def raise_action(self):
        # Acción cuando el botón de Levantar es presionado
        self.suspend_button.setText("Suspender")
        self.suspend_button.clicked.disconnect()
        self.suspend_button.clicked.connect(self.suspend_action)

    def exit_action(self):
        # Acción para el botón Salir
        self.close()

# Función principal para iniciar la aplicación
def main():
    app = QApplication(sys.argv)
    login_window = LoginWindow()
    login_window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
