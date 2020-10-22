from PyQt5 import QtWidgets, QtGui, QtCore


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        widget = QtWidgets.QWidget(self)
        layout = QtWidgets.QVBoxLayout(widget)
        self.graphicsView = QtWidgets.QGraphicsView()
        self.graphicsView.setCursor(QtCore.Qt.CrossCursor)
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsView.setMouseTracking(True)
        layout.addWidget(self.graphicsView)
        self.setCentralWidget(widget)

        self.graphicsView.viewport().installEventFilter(self)

    def eventFilter(self, source, event):
        '''
        if event.type() == QtCore.QEvent.MouseMove:
            if event.buttons() == QtCore.Qt.NoButton:
                print("Simple mouse motion")
            elif event.buttons() == QtCore.Qt.LeftButton:
                print("Left click drag")
            elif event.buttons() == QtCore.Qt.RightButton:
                print("Right click drag")
        '''
        if event.type() == QtCore.QEvent.MouseButtonPress:
            if event.button() == QtCore.Qt.LeftButton:
                print("Press!")
        return super(Window, self).eventFilter(source, event)



if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())