import sys
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QLineEdit
from PyQt6.QtGui import QPalette, QColor

# Create an instance of QApplication
# Create a window
# Set the window title
# Set the geometry of the window (x, y, width, height)
app = QApplication([])
window = QWidget()
window.setWindowTitle("Calcifer")
window.setGeometry(100, 100, 320, 420)

# Create a palette
# Set the color for the Window role to a custom color
# Apply the palette to the window
palette = QPalette()
palette.setColor(QPalette.ColorRole.Window, QColor("#002b36"))
window.setPalette(palette)

# Create a label for the Output
# Move the label to a specific position
# Set the color and font size of the label
output_lbl = QLabel("<h1>Output</h1>", parent=window)
output_lbl.move(20, 80)
output_lbl.setStyleSheet("color: #93a1a1; font-size: 20px;")
# Create a label for the History
# Move the label to a specific position
# Set the color and font size of the label
history_lbl = QLabel("<h1>History</h1>", parent=window)
history_lbl.move(20, 130)
history_lbl.setStyleSheet("color: #93a1a1; font-size: 12px;")
# Create an input box
# Move the input box to a specific position
# Set the color and font size of the input box and remove the border
inputBox = QLineEdit(window)
inputBox.setGeometry(20, 10, 160, 100)
inputBox.setStyleSheet("border: none; background-color: #002b36; color: #93a1a1; font-size: 20px;")

# Show the window
# Exit the application when the window is closed
window.show()
sys.exit(app.exec())

#002b36 
# primary 1

#003b44
# primary 2

#bca600 
# secondary 1

#93a1a1
# text 1