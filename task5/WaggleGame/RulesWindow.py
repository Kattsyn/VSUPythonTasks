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
        Waggle Game Rules:
        - Move pieces by jumping over others.
        - Try to leave only one piece on the board.
        - Use strategic moves to achieve your goal.
        ''')
        layout.addWidget(self.rules_label)

        self.close_button = QPushButton('Close')
        self.close_button.clicked.connect(self.close)
        layout.addWidget(self.close_button)

        self.setLayout(layout)
