import sys
from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QVBoxLayout, QLabel

class CustomDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Custom Dialog")

        layout = QVBoxLayout()

        label = QLabel("This is a custom dialog.")
        layout.addWidget(label)

        button = QPushButton("Close")
        button.clicked.connect(self.close)
        layout.addWidget(button)

        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = CustomDialog()
    dialog.exec_()
