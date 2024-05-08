from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import Qt


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

    def keyPressEvent(self, event):
        if event.text():
            print("Pressed key:", event.text())
        else:
            print("Pressed key:", event.key())


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec_())