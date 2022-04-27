import sys
import windows.window1
import QSSLoader

from PyQt5.QtWidgets import QApplication, QMainWindow
#from qt_material import apply_stylesheet
import qdarkstyle

if __name__ == '__main__':
  app = QApplication(sys.argv)
  MainWindow = QMainWindow()
  ui = windows.window1.Ui_Form()
  ui.setupUi(MainWindow)

  #设置程序的皮肤
  #style_file = './style.qss'
  #style_sheet = QSSLoader.read_qss_file(style_file)
  #window.setStyleSheet(style_sheet)

  #apply_stylesheet(app, theme='dark_teal.xml')

  app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

  MainWindow.show()
  sys.exit(app.exec_())