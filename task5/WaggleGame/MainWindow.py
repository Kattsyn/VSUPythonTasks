import os
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QPushButton, QWidget, QLabel, QVBoxLayout, \
    QHBoxLayout, QMessageBox, QComboBox, QMenuBar, QAction, QMenu
from PyQt5.QtCore import Qt
from Game import Game
from RulesWindow import RulesWindow
from SettingsWindow import SettingsWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Waggle Game')
        self.setGeometry(100, 100, 600, 600)
        self.selected_color = "blue"
        self.level_files = self.get_level_files()
        self.initUI()
        self.initMenuBar()

    def get_level_files(self):
        levels_dir = 'levels'
        return [f for f in os.listdir(levels_dir) if os.path.isfile(os.path.join(levels_dir, f))]

    def initUI(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()

        self.grid_layout = QGridLayout()
        self.layout.addLayout(self.grid_layout)

        self.central_widget.setLayout(self.layout)
        self.game = None

    def initMenuBar(self):
        menubar = self.menuBar()

        gameMenu = menubar.addMenu('Game')

        newGameMenu = QMenu('New Game', self)
        self.level_actions = []
        for i, level_file in enumerate(self.level_files):
            level_action = QAction(f'Level {i + 1}', self)
            level_action.triggered.connect(lambda checked, level=i + 1: self.load_level(level))
            newGameMenu.addAction(level_action)
            self.level_actions.append(level_action)

        rulesAction = QAction('Rules', self)
        rulesAction.triggered.connect(self.show_rules)
        settingsAction = QAction('Settings', self)
        settingsAction.triggered.connect(self.show_settings)
        restartAction = QAction('Restart', self)
        restartAction.triggered.connect(self.reset_level)

        gameMenu.addMenu(newGameMenu)
        gameMenu.addAction(rulesAction)
        gameMenu.addAction(settingsAction)
        gameMenu.addSeparator()
        gameMenu.addAction(restartAction)

    def load_level(self, level):
        self.game = Game(level)
        self.update_board()

    def reset_level(self):
        if self.game:
            level = self.game.level
            self.game = Game(level)
            self.update_board()

    def update_board(self):
        for i in reversed(range(self.grid_layout.count())):
            self.grid_layout.itemAt(i).widget().setParent(None)

        for i in range(self.game.size):
            for j in range(self.game.size):
                btn = QPushButton('')
                if self.game.board[i][j] == 1:
                    btn.setStyleSheet(f"background-color: {self.selected_color}")
                    if self.game.selected and self.game.selected == (i, j):
                        btn.setStyleSheet("background-color: grey")
                btn.clicked.connect(lambda _, x=i, y=j: self.make_move(x, y))
                self.grid_layout.addWidget(btn, i, j)
                btn.setFixedSize(50, 50)

    def make_move(self, row, col):
        if self.game.selected:
            x1, y1 = self.game.selected
            if self.game.is_valid_move(x1, y1, row, col):
                self.game.move(x1, y1, row, col)
                if self.game.check_win():
                    QMessageBox.information(self, 'Waggle Game', 'Ты победил!')
                self.game.selected = (row, col)
            else:
                self.game.selected = None
        else:
            if self.game.board[row][col] == 1:
                self.game.selected = (row, col)
        self.update_board()

    def show_rules(self):
        self.rules_window = RulesWindow(self)
        self.rules_window.show()

    def show_settings(self):
        self.settings_window = SettingsWindow(self, current_color=self.selected_color)
        self.settings_window.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
