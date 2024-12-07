
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QVBoxLayout, QPushButton, QLineEdit, QDialog, QVBoxLayout, QLabel, QTextEdit
from PyQt5.QtCore import Qt

class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Modern Calculator")
        self.setFixedSize(320, 520)
        self.setStyleSheet("background-color: #222831;")  
        self.history = []  
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self.layout = QVBoxLayout()
        self._centralWidget.setLayout(self.layout)
        self.display = QLineEdit()
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)
        self.display.setStyleSheet("""
            background-color: #393E46;
            color: #EEEEEE;
            font-size: 26px;
            padding: 15px;
            border: none;
            border-radius: 5px;
            """)
        self.layout.addWidget(self.display)
        self.buttonsLayout = QGridLayout()
        self.layout.addLayout(self.buttonsLayout)
        buttons = [
            'History', '%', 'Clear', 'DEL',
            '7', '8', '9', '÷',
            '4', '5', '6', '×',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]
        row, col = 0, 0
        for button_text in buttons:
            button = QPushButton(button_text)
            button.setFixedSize(60, 60)
            button.setStyleSheet(self.button_style(button_text))
            button.clicked.connect(lambda checked, text=button_text: self.on_button_click(text))
            self.buttonsLayout.addWidget(button, row, col)
            col += 1
            if col > 3:  
                col = 0
                row += 1
    def button_style(self, text):
        if text.isdigit() or text == '.':
            return """
                background-color: #00ADB5;  
                color: #ffffff;
                font-size: 20px;
                border-radius: 10px;
                """
        elif text in "÷×-+%":
            return """
                background-color: #FF5722;
                color: #ffffff;
                font-size: 20px;
                border-radius: 10px;
                """
        elif text == "=":
            return """
                background-color: #009688;  
                color: #ffffff;
                font-size: 20px;
                border-radius: 10px;
                """
        elif text == "Clear": 
            return """
                background-color: #F44336;  
                color: #ffffff;
                font-size: 20px;
                border-radius: 10px;
                """
        elif text == "DEL":  
            return """
                background-color: #FFA000;  
                color: #ffffff;
                font-size: 20px;
                border-radius: 10px;
                """
        elif text == "History":  
            return """
                background-color: #3A3F47;  
                color: #ffffff;
                font-size: 20px;
                border-radius: 10px;
                """

    def on_button_click(self, text):
        if text == "=":
            self.calculate()
        elif text == "Clear":
            self.display.clear()
        elif text == "DEL":
            current_text = self.display.text()
            self.display.setText(current_text[:-1])
        elif text == "÷":
            self.display.setText(self.display.text() + "/")
        elif text == "×":
            self.display.setText(self.display.text() + "*")
        elif text == "%":
            current_text = self.display.text()
            self.display.setText(current_text + "/100")  
        elif text == "History":
            self.show_history()
        else:
            self.display.setText(self.display.text() + text)

    def calculate(self):
        try:
            expression = self.display.text()
            result = str(eval(expression))
            self.display.setText(result)
            self.history.append(f"{expression} = {result}") 
        except:
            self.display.setText("Error")

    def show_history(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("History")
        dialog.setFixedSize(300, 400)
        layout = QVBoxLayout()
        history_text = QTextEdit()
        history_text.setReadOnly(True)
        history_text.setStyleSheet("""
            background-color: #393E46;
            color: #EEEEEE;
            font-size: 16px;
            padding: 10px;
            """)
        history_text.setText("\n".join(self.history))
        layout.addWidget(history_text)
        dialog.setLayout(layout)
        dialog.exec_() 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec_())
