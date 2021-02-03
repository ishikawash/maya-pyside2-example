import sys
import assets
from PySide2.QtCore import QFile
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QMainWindow, QWidget

class MainWindow(QMainWindow):
    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)
        ui = self.__loadUI()
        self.setCentralWidget(ui)
        self.__ui = ui
        self.__ui.pushButton.clicked.connect(self.close)
    
    def __loadUI(self):
        loader = QUiLoader()
        file = QFile(":/ui/Mainwindow.ui")
        try:
            file.open(QFile.ReadOnly)
            return loader.load(file)
        finally:
            file.close()

def setup():
    from maya import OpenMayaUI as omui
    import pymel.core as pm
    from shiboken2 import wrapInstance
    def openWindow(_):
        mayaMainWindowPtr = omui.MQtUtil.mainWindow() 
        mayaMainWindow = wrapInstance(long(mayaMainWindowPtr), QWidget) 
        window = MainWindow(mayaMainWindow)
        window.show()
    main_window_name = pm.language.melGlobals['gMainWindow']
    menu = pm.menu(u"Example", parent=main_window_name)
    pm.menuItem(label=u"Open...", command=openWindow, parent=menu)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
