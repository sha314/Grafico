import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QPushButton, QAction, QToolBar, QDesktopWidget
from PyQt5.QtCore import QSize    
from PyQt5.QtGui import QIcon
from PyQt5 import Qt



from PyQt5.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QVBoxLayout,
    QPushButton,
    QWidget,
    QFileSystemModel,
    QTreeView,
    QTableWidget,
    QTableWidgetItem
)

from PyQt5.QtWidgets import QTableView, QApplication
from PyQt5.QtCore import QAbstractTableModel, Qt, QModelIndex

from PyQt5.QtWidgets import QMenuBar, QMenu, QAction

from PyQt5 import QtGui

from PyQt5.QtCore import(
    QDir
)


import pandas as pd
import matplotlib.pyplot as plt


import dataframe_model


ProjectDirectory="./project"


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle("Grafico") 
        self.setMinimumSize(QSize(500, 300))
        screen = QDesktopWidget().screenGeometry()
        self.setGeometry(0, 0, int(screen.width()*.8), int(screen.height()*.8))  
        

        # Add button widget
        # pybutton = QPushButton('Pyqt', self)
        # pybutton.clicked.connect(self.clickMethod)
        # pybutton.resize(100,32)
        # pybutton.move(130, 30)        
        # pybutton.setToolTip('This is a tooltip message.')  


        self.main_widget = QtWidgets.QWidget(self)
        self.main_widget.setFocus()
        self.setCentralWidget(self.main_widget)
        layout = QtWidgets.QHBoxLayout(self.main_widget)

        layout.addLayout(self.get_side_panel_ui())
        layout.addLayout(self.get_work_panel_ui())


        self._create_menubar()
        self._createToolBars()

    def _createToolBars(self):
        # Create upper toolbar with menu options
        tb = QToolBar(self)
        menu = QMenu(self)
        menu_plot = QAction("Plot", self)
        menu_plot.setStatusTip("Select a file to use as a database")
        menu_plot.triggered.connect(self.plot_graph)
        menu.addAction(menu_plot)
        tb.addWidget(menu)
        tb.setAllowedAreas(Qt.TopToolBarArea)
        tb.setFloatable(False)
        tb.setMovable(False)
        self.addToolBar(tb)


    def plot_graph(self):
        print("plotting graph")
        graph_path = ProjectDirectory + "/Graph1.pdf"
        print(self.data_frame)
        self.data_frame.plot(x='X',y='x^2')
        plt.savefig(graph_path)
        


        pass


    def get_work_panel_ui(self):

        layout = QVBoxLayout()
        self.table_widget = QTableView()
 

        layout.addWidget(self.table_widget)


        self.load_data()


        return layout

    # def dataframe_generation_from_table(self, table):
    #     number_of_rows = table.rowCount()
    #     number_of_columns = table.columnCount()

    #     tmp_df = pd.DataFrame( 
    #                 columns=['Date', str(self.final_lvl_of_analysis), 'Value'], # Fill columnets
    #                 index=range(number_of_rows) # Fill rows
    #                 ) 

    #     for i in range(number_of_rows):
    #         for j in range(number_of_columns):
    #             tmp_df.ix[i, j] = table.item(i, j).data()

    #     return tmp_df

    def load_data(self):

        data_path="./project/test.csv"
        self.data_frame = pd.read_csv(data_path)

        # view = QTableView()
        # view.resize(800, 500)
        self.table_widget.horizontalHeader().setStretchLastSection(True)
        self.table_widget.setAlternatingRowColors(True)
        self.table_widget.setSelectionBehavior(QTableView.SelectRows)

        model = dataframe_model.PandasModel(self.data_frame)
        self.table_widget.setModel(model)
        self.table_widget.show()

        pass


    def get_side_panel_ui(self):
        layout = QVBoxLayout()
        model = QFileSystemModel()
        model.setRootPath(QDir.currentPath())

        tree =  QTreeView()
        tree.setModel(model)

        tree.setRootIndex(model.index(QDir.currentPath()))
        

        layout.addWidget(tree)
        return layout
    
    # def _createToolBars(self):
    #     # Using a title
    #     fileToolBar = self.addToolBar("File")
    #     # Using a QToolBar object
    #     editToolBar = QToolBar("Edit", self)
    #     self.addToolBar(editToolBar)
    #     # Using a QToolBar object and a toolbar area
    #     helpToolBar = QToolBar("Help", self)
    #     # self.addToolBar(Qt.LeftToolBarArea, helpToolBar)

    def _create_menubar(self):
        # Create new action
        newAction = QAction(QIcon('new.png'), '&New', self)        
        newAction.setShortcut('Ctrl+N')
        newAction.setStatusTip('New document')
        newAction.triggered.connect(self.newCall)

        # Create new action
        openAction = QAction(QIcon('open.png'), '&Open', self)        
        openAction.setShortcut('Ctrl+O')
        openAction.setStatusTip('Open document')
        openAction.triggered.connect(self.openCall)

        # Create exit action
        exitAction = QAction(QIcon('exit.png'), '&Exit', self)        
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.exitCall)

        # Create menu bar and add action
        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu('&File')
        fileMenu.addAction(newAction)
        fileMenu.addAction(openAction)
        fileMenu.addAction(exitAction)



         # Create menu bar and add action
        editMenu = menuBar.addMenu('&Edit')
        editMenu.addAction(newAction)
        editMenu.addAction(openAction)
        editMenu.addAction(exitAction)


        viewMenu = menuBar.addMenu('&View')
        viewMenu.addAction(newAction)
        viewMenu.addAction(openAction)
        viewMenu.addAction(exitAction)


        aboutMenu = menuBar.addMenu('&About')
        aboutMenu.addAction(newAction)
        aboutMenu.addAction(openAction)
        aboutMenu.addAction(exitAction)




    def openCall(self):
        print('Open')

    def newCall(self):
        print('New')

    def exitCall(self):
        print('Exit app')

    # def clickMethod(self):
    #     print('PyQt')

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit( app.exec_() )