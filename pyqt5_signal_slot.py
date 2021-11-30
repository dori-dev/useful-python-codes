"""Signal and Slot in PyQt5
"""

import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QVBoxLayout


def show_message():
    """Slot function
    for show and hide message
    """

    text = "" if message_label.text() else "Hello World!"
    message_label.setText(text)


app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Signal & Slot")
window.setGeometry(0, 0, 250, 90)
layout = QVBoxLayout()

message_button = QPushButton("Show Message!")
message_button.clicked.connect(show_message)
layout.addWidget(message_button)

message_label = QLabel("")
layout.addWidget(message_label)


window.setLayout(layout)


window.show()
sys.exit(app.exec_())
