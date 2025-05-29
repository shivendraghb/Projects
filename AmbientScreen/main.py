import sys
from PyQt5.QtWidgets import (QApplication, QWidget)
from PyQt5.QtCore import QTimer, Qt

class AmbientScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.hue = 0
        self.initUI()

    def initUI(self):
        self.setWindowTitle("AmbientScreen")
        # Uncomment below for full screen
        # self.showFullScreen()
        self.resize(600, 400) # default window size
        self.show()

        # timer to update background color
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_display)
        self.timer.start(10)

        self.update_display()

    def update_display(self):

        self.hue = (self.hue + 1) % 360
        color = f"hsl({self.hue}, 70%, 60%)"
        self.setStyleSheet(f"background-color: {color}")

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()


if __name__ == "__main__":

    app = QApplication(sys.argv)

    screen = AmbientScreen()

    sys.exit(app.exec_())
