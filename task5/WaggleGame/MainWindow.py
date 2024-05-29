import os
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QPushButton, QWidget, QLabel, QVBoxLayout, \
    QHBoxLayout, QMessageBox
from PyQt5.QtCore import Qt
import PyQt5

from task5.WaggleGame.Game import Game

# Установите переменную окружения для пути к плагинам Qt
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = os.path.join(os.path.dirname(PyQt5.__file__), 'Qt', 'plugins')


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Waggle Game')
        self.setGeometry(100, 100, 600, 600)
        self.initUI()

    def initUI(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()

        self.level_select_layout = QHBoxLayout()
        self.level_label = QLabel("Select Level: ")
        self.level_select_layout.addWidget(self.level_label)
        self.level_buttons = [QPushButton(f'Level {i + 1}') for i in range(3)]
        for button in self.level_buttons:
            button.clicked.connect(self.load_level)
            self.level_select_layout.addWidget(button)

        self.layout.addLayout(self.level_select_layout)

        self.grid_layout = QGridLayout()
        self.layout.addLayout(self.grid_layout)

        self.reset_button = QPushButton("Reset Level")
        self.reset_button.clicked.connect(self.reset_level)
        self.layout.addWidget(self.reset_button)

        self.central_widget.setLayout(self.layout)
        self.game = None

    def load_level(self):
        sender = self.sender()
        level = int(sender.text().split()[-1])
        self.game = Game(level)
        self.update_board()

    def reset_level(self):
        if self.game:
            self.load_level()

    def update_board(self):
        for i in reversed(range(self.grid_layout.count())):
            self.grid_layout.itemAt(i).widget().setParent(None)

        for i in range(self.game.size):
            for j in range(self.game.size):
                btn = QPushButton('')
                if self.game.board[i][j] == 1:
                    btn.setStyleSheet("background-color: blue")
                btn.clicked.connect(lambda _, x=i, y=j: self.make_move(x, y))
                self.grid_layout.addWidget(btn, i, j)
                btn.setFixedSize(50, 50)

    def make_move(self, row, col):
        if self.game.selected:
            x1, y1 = self.game.selected
            if self.game.is_valid_move(x1, y1, row, col):
                self.game.move(x1, y1, row, col)
                if self.game.check_win():
                    QMessageBox.information(self, 'Waggle Game', 'You won!')
            self.game.selected = None
        else:
            if self.game.board[row][col] == 1:
                self.game.selected = (row, col)
        self.update_board()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
