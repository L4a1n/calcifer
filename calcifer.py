import sys
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QLineEdit
from PyQt6.QtGui import QPalette, QColor, QFontMetrics, QGuiApplication
import math


# Create a class that inherits from QWidget
class Init_QWidget(QWidget):
    def __init__(self):
        super().__init__()
    def event(self, event):
        return super().event(event)

               
class Calcifer():
    def __init__(self):
        # Create an instance of QApplication
        # Create a window
        # Set the window title
        # Set the geometry of the window (x, y, width, height)
        self.app = QApplication([])
        self.window = Init_QWidget()
        self.window.setWindowTitle("Calcifer")
        self.window.setGeometry(100, 100, 320, 420)

        # Create a palette
        # Set the color for the Window role to a custom color
        # Apply the palette to the window
        self.palette = QPalette()
        self.palette.setColor(QPalette.ColorRole.Window, QColor("#002b36"))
        self.window.setPalette(self.palette)

        # Call the init_lbl() 
        # and init_input() methods
        # Show the window
        # Exit the application upon closing the window
        self.init_input()
        self.init_lbl()
        self.window.show()
        sys.exit(self.app.exec())

    def init_lbl(self):
        # Create a label for the Output
        # Move the label to a specific position
        # Set the color and font size of the label
        self.output_lbl = QLabel("<h1> 0 </h1>", parent=self.window)
        self.output_lbl.move(20, 80)
        self.output_lbl.setStyleSheet("color: #93a1a1; font-size: 20px;")
        # Create a label for the History
        # Move the label to a specific position
        # Set the color and font size of the label
        self.history_lbl = QLabel("<h1> Output History... </h1>", parent=self.window)
        self.history_lbl.move(20, 130)
        self.history_lbl.setStyleSheet("color: #93a1a1; font-size: 12px;")

    def calculate_and_update(self, text):
        # Calculate the result of the expression
        try:
            result = str(eval(text, {"__builtins__": None}, {"math": math}))
        except Exception as e:
            if text == "":
                result = "0"
            else:
                result = text
    
        # Update the text of the output label
        self.output_lbl.setText("<h1>" + result + "</h1>")
    
        # Calculate the width of the text
        font_metrics = QFontMetrics(self.output_lbl.font())
        text_width = font_metrics.horizontalAdvance(result)
    
        # Set the width of the label
        self.output_lbl.setFixedWidth(text_width*3)

    def init_input(self):
        # Create an input box
        # Move the input box to a specific position
        # Set the color and font size of the input box and remove the border
        # Connect the input box to the update_output_lbl() method
        self.inputBox = QLineEdit(self.window)
        self.inputBox.setGeometry(20, 10, 160, 60)
        self.inputBox.setStyleSheet("border: none; background-color: #002b36; color: #93a1a1; font-size: 20px;")
        self.inputBox.textChanged.connect(self.calculate_and_update)


# Create an instance of the Calcifer class
calcifer = Calcifer()    

#002b36 
# primary 1

#003b44
# primary 2

#bca600 
# secondary 1

#93a1a1
# text 1