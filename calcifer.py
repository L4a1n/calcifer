import sys, math
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QLineEdit
from PyQt6.QtGui import QPalette, QColor, QFontMetrics


class load_config():
    def __init__(self):
        pass


# Create a class that inherits from QWidget
class Init_QWidget(QWidget):
    def __init__(self):
        super().__init__()
    def event(self, event):
        return super().event(event)


# Main class
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
        # init the history list
        # Show the window
        # Exit the application upon closing the window
        self.init_input()
        self.init_lbl()
        self.history = []
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
        # Set the width and height of the label
        self.history_lbl = QLabel("", parent=self.window)
        self.history_lbl.move(20, 130)
        self.history_lbl.setStyleSheet("color: #93a1a1;")
        self.history_lbl.setFixedWidth(280)
        self.history_lbl.setFixedHeight(500)


    def calculate_and_update(self, text):
        # Calculate the result of the expression
        try:
            # If the expression is valid, calculate the result
            result = str(eval(text, {"__builtins__": None}, {"math": math}))
        # If the expression is invalid, set the result to custom text
        except Exception as e:
            if text == "":
                result = "0"
            elif text == "help":
                result = "OPERATORS:"
                self.history_lbl.setText("+ Addition \n - Subtraction \n * Multiplication\n / Division\n ** Potentiate")
            else:
                result = text
        # Update the text of the output label
        self.output_lbl.setText("<h1>"+result+"</h1>")
        # Calculate the width of the text
        font_metrics = QFontMetrics(self.output_lbl.font())
        text_width = font_metrics.horizontalAdvance(result)
        # Set the width of the label
        self.output_lbl.setFixedWidth(text_width*3)


    def update_history(self):
        # Get the text of the input box
        # Get the text of the output label
        # Remove the HTML tags from the output label text
        # Add the expression and result to temp string
        # Append the temp string to the history list
        text = self.inputBox.text()
        result = self.output_lbl.text()
        result = result.replace("<h1>", "")
        result = result.replace("</h1>", "")
        temp = f"{text}={result}"
        self.history.append(temp)
        # Check if the history list has one or less items
        # If it does, join the items without HTML tags
        # Else, join the items with HTML tags
        if len(self.history) <= 1:
            history_str = "".join(self.history)
        else:
            history_str = "<h1>".join(self.history)+"</h1>"
        # Set the text of the history label to the joined string
        self.history_lbl.setText(history_str)
    

    def init_input(self):
        # Create an input box
        # Move the input box to a specific position
        # Set the color and font size of the input box and remove the border
        # Connect the input box to the calculate_and_update() method
        # Connect the input box to the update_history() method when the return/enter key is pressed
        self.inputBox = QLineEdit(self.window)
        self.inputBox.setGeometry(20, 10, 160, 60)
        self.inputBox.setStyleSheet("border: none; background-color: #002b36; color: #93a1a1; font-size: 20px;")
        self.inputBox.textChanged.connect(self.calculate_and_update)
        self.inputBox.returnPressed.connect(self.update_history)


# Create an instance of the Calcifer class
calcifer = Calcifer()    


# ignore that stuff...

#002b36 
# primary 1

#003b44
# primary 2

#bca600 
# secondary 1

#93a1a1
# text 1