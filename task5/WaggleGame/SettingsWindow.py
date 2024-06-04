from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QComboBox, QPushButton

class SettingsWindow(QDialog):
    def __init__(self, parent=None, current_color="blue"):
        super().__init__(parent)
        self.setWindowTitle('Game Settings')
        self.setGeometry(100, 100, 400, 300)
        self.initUI(current_color)

    def initUI(self, current_color):
        layout = QVBoxLayout()

        self.color_label = QLabel('Select Checker Color:')
        layout.addWidget(self.color_label)

        self.color_combo_box = QComboBox()
        self.color_combo_box.addItems(["Blue", "Red", "Green", "Yellow"])
        self.color_combo_box.setCurrentText(current_color.capitalize())
        layout.addWidget(self.color_combo_box)

        self.apply_button = QPushButton('Apply')
        self.apply_button.clicked.connect(self.apply_settings)
        layout.addWidget(self.apply_button)

        self.close_button = QPushButton('Close')
        self.close_button.clicked.connect(self.close)
        layout.addWidget(self.close_button)

        self.setLayout(layout)

    def apply_settings(self):
        selected_color = self.color_combo_box.currentText().lower()
        self.parent().selected_color = selected_color
        self.parent().update_board()
        self.close()
