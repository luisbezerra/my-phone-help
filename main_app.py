import sys
import requests
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QListWidget

class TechUnionApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Phone help - Painel de Suporte")
        self.resize(400, 500)

        # Layout Principal
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        self.label = QLabel("Marcas Disponíveis no Servidor:")
        self.layout.addWidget(self.label)

        self.list_widget = QListWidget()
        self.layout.addWidget(self.list_widget)

        # Chama a função para buscar dados do Django
        self.carregar_marcas()

    def carregar_marcas(self):
        try:
            # Endpoint padrão do Django (vamos precisar criar a API no próximo passo)
            response = requests.get("http://127.0.0")
            if response.status_code == 200:
                marcas = response.json()
                for marca in marcas:
                    self.list_widget.addItem(marca['name'])
            else:
                self.list_widget.addItem("Erro ao conectar com o servidor.")
        except Exception as e:
            self.list_widget.addItem(f"Servidor Offline: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TechUnionApp()
    window.show()
    sys.exit(app.exec())
