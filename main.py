import sys
from PyQt5.QtWidgets import (QApplication, QLabel,
                            QWidget, QPushButton, QVBoxLayout, QHBoxLayout)
from PyQt5.QtCore import QTimer, QTime, Qt

class Stopwatch(QWidget):
    def __init__(self):
        super().__init__()
        self.time = QTime(0, 0, 0, 0)
        self.time_label = QLabel("00:00:00.00", self)
        self.start_button = QPushButton("Start", self)
        self.stop_button = QPushButton("Stop", self)
        self.reset_button = QPushButton("Reset", self)
        self.timer = QTimer(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("StopWatch")

        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        # vbox.addWidget(self.start_button)
        # vbox.addWidget(self.stop_button)
        # vbox.addWidget(self.reset_button)

        self.setLayout(vbox)

        self.time_label.setAlignment(Qt.AlignCenter)

        hbox = QHBoxLayout()

        hbox.addWidget(self.start_button)
        hbox.addWidget(self.stop_button)
        hbox.addWidget(self.reset_button)

        vbox.addLayout(hbox)
        # hbox.addLayout(vbox)

        self.setStyleSheet("""
            QPushButton, QLabel{
                padding: 20px;
                font-weight: bold;
                font-family: garamond
            }
            QPushButton{
                font-size: 25px;
            }
            QLabel{
                font-size: 50px;
                background-color: #edcc37;
                border-radius: 20px;
            }
        """)

        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)
        self.reset_button.clicked.connect(self.reset)
        self.timer.timeout.connect(self.update_display)

    def start(self):
        self.timer.start(10)

    def stop(self):
        self.timer.stop()

    def reset(self):
        self.timer.stop()
        self.time = QTime(0, 0, 0, 0)
        self.time_label.setText(self.format_time(self.time))

    def format_time(self, time):
        hours = time.hour()
        minutes = time.minute()
        seconds = time.second()
        milliseconds = time.msec() // 10
        return f"{hours:02}:{minutes:02}:{seconds:02}.{milliseconds:02}"

    def update_display(self):
        self.time = self.time.addMSecs(10)
        self.time_label.setText(self.format_time(self.time))

        # dynamic background color change using HSV model
        elapsed_ms = self.time.hour() * 3600000 + self.time.minute() * 60000 + self.time.second() * 1000 + self.time.msec()
        hue = (elapsed_ms // 10) % 360 # keep hue in range 0-359
        color = f"hsl({hue}, 70%, 60%)" # saturation and lightness for smooth color
        self.time_label.setStyleSheet(f"""
            QLabel {{
                font-size: 50px;
                background-color: {color};
                border-radius: 20px;
                padding: 20px;
                font-weight: bold;
                font-family: garamond;
            }}
        """)

if __name__ == "__main__":
    #this is for command line arguments which we will not be using but
    #to make the code future-proof if we do it in the future
    app = QApplication(sys.argv)

    stopwatch = Stopwatch()
    stopwatch.show() # shows the window for only a brief second

    # execute() method : this method starts the main event loop and handles event
    sys.exit(app.exec_())
