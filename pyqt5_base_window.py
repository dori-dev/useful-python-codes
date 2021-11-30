"""Base PyQt5 Window
"""

import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Mohammad Dori")
window.setGeometry(500, 500, 400, 70)
name_label = QLabel("<h1> Hello I am Mohammad </h1>", parent=window)
name_label.move(60, 15)

window.show()

sys.exit(app.exec_())
