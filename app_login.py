import sys
import requests
import subprocess
import hashlib
from PySide6.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QWidget, 
                             QLabel, QLineEdit, QPushButton, QMessageBox)

# --- FUNÇÃO DE SEGURANÇA (HWID) ---
def get_hwid():
    try:
        # Pega o UUID da BIOS/Placa-mãe (ID Único do PC)
        cmd = 'wmic csproduct get uuid'
        uuid = subprocess.check_output(cmd, shell=True).decode().split('\n')[1].strip()
        return hashlib.sha256(uuid.encode()).hexdigest()
    except:
        return "ID_NAO_CAPTURADO"

# --- INTERFACE DO EXECUTÁVEL ---
class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Phone help - Login Seguro")
        self.setFixedSize(300, 350)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        # Campos de Login
        self.layout.addWidget(QLabel("Usuário:"))
        self.input_user = QLineEdit()
        self.layout.addWidget(self.input_user)

        self.layout.addWidget(QLabel("Senha:"))
        self.input_pass = QLineEdit()
        self.input_pass.setEchoMode(QLineEdit.Password) # Esconde a senha
        self.layout.addWidget(self.input_pass)

        # Botão de Login
        self.btn_login = QPushButton("Validar Licença e Entrar")
        self.btn_login.clicked.connect(self.realizar_login)
        self.layout.addWidget(self.btn_login)

        # Exibe o HWID atual apenas para conferência
        self.layout.addWidget(QLabel(f"Seu ID: {get_hwid()[:15]}..."))

    def realizar_login(self):
        user = self.input_user.text()
        pw = self.input_pass.text()
        hwid = get_hwid()

        # Dados para enviar ao Django
        dados = {
            "username": user,
            "password": pw,
            "hwid": hwid
        }

        try:
            # Envia para a API que criamos no Django
            response = requests.post("http://localhost:8000/auth/login-hwid/", json=dados)
            
            if response.status_code == 200:
                msg = response.json().get('message')
                QMessageBox.information(self, "Sucesso", f"{msg}\nAcesso Liberado!")
                # Aqui você abriria a tela das Marcas que fizemos antes
            else:
                erro = response.json().get('message', 'Erro desconhecido')
                QMessageBox.critical(self, "Bloqueado", f"Erro: {erro}")
        
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Servidor Offline ou Erro de Rede: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())
