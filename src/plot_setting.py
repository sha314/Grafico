
from PyQt5.QtWidgets import QMainWindow, QWidget, QPushButton, QAction, QToolBar, QDesktopWidget, QDialog



from PyQt5.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QVBoxLayout,
    QPushButton,
    QWidget,
    QFileSystemModel,
    QTreeView,
    QTableWidget,
    QTableWidgetItem,
    QDialogButtonBox,
    QLabel
)



class PlotDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("HELLO!")

        QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        # QBtn = QDialogButtonBox.Next | QDialogButtonBox.Prev

        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        message = QLabel("Something happened, is that OK?")
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)

    def page1(self):
        print("choose columns")
        pass

    def page2(self):

        pass
