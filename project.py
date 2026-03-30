import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QAction, QFileDialog
from PyQt5.QtGui import QIcon


class TextEditor(QMainWindow):
    def __init__(self):  # should be __init__, not _init_
        super().__init__()  # same here+
        self.init_ui()  # should call init_ui, not _init_vi

    def init_ui(self):
        self.text_edit = QTextEdit(self)
        self.setCentralWidget(self.text_edit)

        # File actions
        new_file_action = QAction(QIcon('icons/new.png'), 'New', self)
        new_file_action.setShortcut('Ctrl+N')
        new_file_action.triggered.connect(self.new_file)

        open_file_action = QAction(QIcon('icons/open.png'), 'Open', self)
        open_file_action.setShortcut('Ctrl+O')  # use 'O', not '0'
        open_file_action.triggered.connect(self.open_file)

        save_file_action = QAction(QIcon('icons/save.png'), 'Save', self)
        save_file_action.setShortcut('Ctrl+S')
        save_file_action.triggered.connect(self.save_file)

        exit_action = QAction(QIcon('icons/exit.png'), 'Exit', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.triggered.connect(self.close)

        # Menu bar
        file_menu = self.menuBar().addMenu('File')
        file_menu.addAction(new_file_action)
        file_menu.addAction(open_file_action)
        file_menu.addAction(save_file_action)
        file_menu.addSeparator()
        file_menu.addAction(exit_action)

        self.setWindowTitle('Text Editor')
        self.resize(600, 400)
        self.show()

    def new_file(self):
        self.text_edit.clear()

    def open_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, 'Open file', '', 'Text files (*.txt);;All files (*.*)')
        if file_path:
            with open(file_path, 'r') as f:
                self.text_edit.setPlainText(f.read())

    def save_file(self):
        file_path, _ = QFileDialog.getSaveFileName(self, 'Save file', '', 'Text files (*.txt);;All files (*.*)')
        if file_path:
            with open(file_path, 'w') as f:
                f.write(self.text_edit.toPlainText())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    editor = TextEditor()
    sys.exit(app.exec_())  # should be exec_(), not exed()
