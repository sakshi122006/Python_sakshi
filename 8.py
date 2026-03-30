import sys 
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QPushButton  # type: ignore
class SimpleGUI(QWidget):
     def __init__(self): 
        super().__init__() 
        self.initUI()
        def initUI(self): self.setWindowTitle('Simple GUI with QTextEdit') 
        self.setGeometry(100, 100, 400, 300) 
        layout = QVBoxLayout(self)
        self.text_edit1 = QTextEdit(self)
        layout.addWidget(self.text_edit1)
        self.text_edit2 = QTextEdit(self)
        layout.addWidget(self.text_edit2)
        button1 = QPushButton('Button 1', self) 
        layout.addWidget(button1)