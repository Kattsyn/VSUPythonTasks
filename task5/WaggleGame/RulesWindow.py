from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton


class RulesWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Game Rules')
        self.setGeometry(100, 100, 400, 300)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.rules_label = QLabel('''
        Правила игры Вогл:
        - Перемещайте фигуры, перепрыгивая через другие.
        - Постарайтесь оставить на доске только одну фигуру.
        - Используйте стратегию, чтобы победить.
        ''')
        layout.addWidget(self.rules_label)

        self.close_button = QPushButton('Close')
        self.close_button.clicked.connect(self.close)
        layout.addWidget(self.close_button)

        self.setLayout(layout)
